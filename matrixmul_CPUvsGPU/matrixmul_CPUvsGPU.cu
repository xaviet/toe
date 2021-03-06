/*
CUDA initialized.
Device : " GeForce GT 1030 "

[512, 512] * [512, 512]
cpu time = 0.944000s 944
gpu time = 0.231000s 231


*/

#include "helper_cuda.h"
#include "stdio.h"
#include "assert.h"
#include "windows.h"
#include "time.h"
#include "cuda_runtime.h"
#include "device_launch_parameters.h"


#if __DEVICE_EMULATION__
bool InitCUDA(void) { return true; }
#else
int InitCUDA(void)
{
  int count = 0;
  int i = 0;
  cudaGetDeviceCount(&count);
  if (count == 0) {
    fprintf(stderr, "There is no device.\n");
    return false;
  }
  cudaDeviceProp prop;
  for (i = 0; i < count; i++) {
    if (cudaGetDeviceProperties(&prop, i) == cudaSuccess) {
      if (prop.major >= 1) {
        break;
      }
    }
  }
  if (i == count) {
    fprintf(stderr, "There is no device supporting CUDA.\n");
    return false;
  }
  cudaSetDevice(i);
  printf("CUDA initialized.\n");
  printf("Device : %s\n", prop.name);
  return(_ConvertSMVer2Cores(prop.major, prop.minor) * prop.multiProcessorCount);
}
#endif

#define aW 2048
#define aH 256
#define bW 256
#define blocknum 32
#define threadnum 1024

typedef struct
{
  int width;
  int height;
  float *element;
}Matrix;
Matrix InitMatrix(int w, int h)
{
  Matrix t;
  t.element = (float *)malloc(w * h * sizeof(float));
  for (int i = 0; i < w*h; i++)
    t.element[i] = (float)(rand()) / RAND_MAX; // 0 to RAND_MAX;
  t.width = w;
  t.height = h;
  return t;
}
Matrix MM(Matrix a, Matrix b)
{
  Matrix t;
  t.element = (float *)malloc(a.height * b.width * sizeof(float));
  t.width = b.width;
  t.height = a.height;
  /*int x;
  int y;
  for (int i = 0; i < t.width * t.height; i++)
  {
    x = i / t.width * a.width;
    y = i - i / t.width * t.width;
    t.element[i] = 0;
    for (int k = 0; k < a.width; k++)
    {
      t.element[i] += a.element[x + k] * b.element[y + b.width * k];
    }
  }*/
  return t;
}
Matrix multiThreadsMM(Matrix matrixa, Matrix matrixb, DWORD dwNumberOfProcessors)
{
  Matrix t;
  t.element = (float *)malloc(matrixa.height * matrixb.width * sizeof(float));
  t.width = matrixb.width;
  t.height = matrixa.height;
  return t;
}
int printMatrix(Matrix* c, int h, int w)
{
  for (int i=0;i<c->height;i++)
  {
    if (i == h)
    {
      break;
    }
    for (int j = 0; j < c->width; j++)
    {
      if (j == w)
      {
        break;
      }
      printf("%16f, ", c->element[i*c->width + j]);
    }
    printf("\n");
  }
  return(0);
}

__global__ static void MatrixMul(float *ma, float *mb, float *mc, int *mp)
{
  int aw = mp[0];
  int bw = mp[2];
  int cw = mp[4];
  int ch = mp[5];
  int tBlock = mp[6];
  int tThread = mp[7];
  const int bid = blockIdx.x;
  const int tid = threadIdx.x;
  int i, x, y;

  for (i = bid * tThread + tid; i < cw * ch; i += tThread * tBlock)
  {
    x = i / cw * aw;
    y = i - i / cw * cw;
    mc[i] = 0;
    for (int k = 0; k < aw; k++)
    {
      mc[i] += ma[x + k] * mb[y + k * bw];
    }
  }
}


int matrixmul_CPUvsGPU(void)
{
  srand(clock());
  int cudaCores = 0;
  if (!(cudaCores = InitCUDA())) {
    return 0;
  }
  printf("Found cudaCores %d\n", cudaCores);
  //定义矩阵
  //int matrixa[N][N] , matrixb[N][N] , matrixc[N][N] , gpuresult[N][N] , matrixd[N][N] ;
  printf("[%d, %d] * [%d, %d]\n", aW, aH, bW, aW);
  Matrix matrixa = InitMatrix(aW, aH);
  printf("matrixa\n");
  printMatrix(&matrixa, 4, 4);
  Matrix matrixb = InitMatrix(bW, aW);
  printf("matrixb\n");
  printMatrix(&matrixb, 4, 4);
  Matrix matrixc;
  Matrix gpuresult = InitMatrix(bW, aH);

  int matrixprop[10];

  //为CPU运算计时

  //CPU矩阵相乘
  int start = clock();
  matrixc = MM(matrixa, matrixb);
  int finish = clock();
  printf("\nmatrixc CPU\n");
  printMatrix(&matrixc, 4, 4);
  printf("cpu time(single thread)\t\t = %fs %d\n", (float)(finish - start) / CLOCKS_PER_SEC, finish - start);

  SYSTEM_INFO sysInfo;
  GetSystemInfo(&sysInfo);
  start = clock();
  Matrix matrixd;
  matrixd = multiThreadsMM(matrixa, matrixb, sysInfo.dwNumberOfProcessors);
  finish = clock();
  printf("\nmatrixd CPU\n");
  printMatrix(&matrixd, 4, 4);
  printf("cpu time(%4d threads)\t\t = %fs %d\n", sysInfo.dwNumberOfProcessors, (float)(finish - start) / CLOCKS_PER_SEC, finish - start);

  start = clock();
  matrixprop[0] = matrixa.width;
  matrixprop[1] = matrixa.height;
  matrixprop[2] = matrixb.width;
  matrixprop[3] = matrixb.height;
  matrixprop[4] = matrixc.width;
  matrixprop[5] = matrixc.height;

  //申请显存
  float *ma, *mb, *mc;
  int *mp;
  int tBlock = 1;
  int tThread = 1;
  for (tBlock = 1; tBlock <= 1024; tBlock *= 2)
  {
    for (tThread = 1; tThread <= 1024; tThread *= 2)
    {
      start = clock();
      gpuresult = InitMatrix(bW, aH);
      cudaMalloc((void**)&ma, sizeof(float) * matrixa.width * matrixa.height);
      cudaMalloc((void**)&mb, sizeof(float) * matrixb.width * matrixb.height);
      cudaMalloc((void**)&mc, sizeof(float) * matrixc.width * matrixc.height);
      cudaMalloc((void**)&mp, sizeof(int) * 10);
      //将数据复制到显存内
      cudaMemcpy(ma, matrixa.element, sizeof(float) * matrixa.width * matrixa.height, cudaMemcpyHostToDevice);
      cudaMemcpy(mb, matrixb.element, sizeof(float) * matrixb.width * matrixb.height, cudaMemcpyHostToDevice);
      matrixprop[6] = tBlock;
      matrixprop[7] = tThread;
      cudaMemcpy(mp, matrixprop, sizeof(int) * 6, cudaMemcpyHostToDevice);
      //调用CUDA函数
      MatrixMul << < tBlock, tThread >> > (ma, mb, mc, mp);
      cudaThreadSynchronize();
      //cutilCheckError( cutStopTimer( timer2));
      //将数据从显存中复制出来
      cudaMemcpy(gpuresult.element, mc, sizeof(float) * gpuresult.width * gpuresult.height, cudaMemcpyDeviceToHost);
      finish = clock();
      //printf("\ngpuresult GPU Block=%d\n", tBlock);
      //printMatrix(&gpuresult, 4, 4);
      //printf("Block=%4d Thread=%4d Result=%f gpu time(%4d CUDA Cores)\t = %fs %4d\n", tBlock, tThread, gpuresult.element[0], cudaCores, (float)(finish - start) / CLOCKS_PER_SEC, finish - start);
      printf("%4d,%4d,\t%4.4f,\t%4d\n", tBlock, tThread, gpuresult.element[0], finish - start);
      float err = 0;
      for (int i = 0; i < gpuresult.width * gpuresult.height; i++)
      {
        //if (matrixc.element[i] != gpuresult.element[i])
        //{
          //printf("ERROR");
        //}
        err += matrixc.element[i] - gpuresult.element[i];
        //printf("%f - %f = %f \n", matrixc.element[i], gpuresult.element[i], err);
      }
      //printf("\nerror: %f\n", err / (gpuresult.width * gpuresult.height));

      cudaFree(ma);
      cudaFree(mb);
      cudaFree(mc);
      cudaFree(mp);
    }
  }

  return 0;
}

__global__ void vectorAdd(float* ga, float* gb, float* gc, int n)
{
  // threadIdx.x means current thread ID in this block
  // blockIdx.x means current block ID
  // blockDim.x means threads[x,y,z] per block
  // gridDim.x means blocks[x,y,z] per grid
  int tIndex = threadIdx.x + threadIdx.y * blockDim.x + blockDim.x * blockDim.y* (blockIdx.x + blockIdx.y * gridDim.x);
  if (tIndex < n)
  {
    gc[tIndex] = ga[tIndex] + gb[tIndex];
  }
}

int initFloatMatrix(float* ma, int mw, int mh)
{
  for (int i = 0; i < mw*mh; i++)
  {
    ma[i] = (float)(rand()) / RAND_MAX; // 0 to RAND_MAX;
  }
  return(0);
}

int printFloatMatrix(float* ma, int mw, int mh)
{
  for (int i = 0; i < mh; i++)
  {
    if (i >= 5)
    {
      break;
    }
    printf("\n");
    for (int j = 0; j < mw; j++)
    {
      if (j >= 5)
      {
        break;
      }
      printf("\t%4.8f\t", ma[i*mw + j]);
    }
  }
  printf("\n");
  return(0);
}

int ex(int mw, int mh)
{
  srand(clock());
  //int cudaCores = 0;
  //if (!(cudaCores = InitCUDA())) 
  //{
  //  printf("GPU Fail");
  //  return 0;
  //}
  //printf("Found cudaCores %d\n", cudaCores);
  float *a, *b, *c, *ga, *gb, *gc;
  int size = mw * mh * sizeof(float);
  cudaMalloc((void **)&ga, size);
  cudaMalloc((void **)&gb, size);
  cudaMalloc((void **)&gc, size);
  a = (float *)malloc(size); 
  initFloatMatrix(a, mw, mh);
  b = (float *)malloc(size); 
  initFloatMatrix(b, mw, mh);
  c = (float *)malloc(size);
  initFloatMatrix(c, mw, mh);
  cudaMemcpy(ga, a, size, cudaMemcpyHostToDevice);
  cudaMemcpy(gb, b, size, cudaMemcpyHostToDevice);
  int start = clock();
  dim3 blocks(65535, 65535, 1);
  dim3 threads(mw, mh, 1);
  vectorAdd << < blocks, threads >> > (ga, gb, gc, mw * mh);
  cudaDeviceSynchronize();
  int stop = clock();
  cudaMemcpy(c, gc, size, cudaMemcpyDeviceToHost);
  printFloatMatrix(a, mw, mh);
  printFloatMatrix(b, mw, mh);
  printFloatMatrix(c, mw, mh);
  printf("spent time: %8d\n",stop-start);
  float sumA = 0;
  float sumB = 0;
  float sumC = 0;
  float sumCPU = 0;
  for (int i = 0; i < (mw*mh); i++)
  {
    sumA += a[i];
    sumB += b[i];
    sumCPU += a[i] + b[i];
    sumC += c[i];
  }
  printf("%4.8f + %4.8f = \n", sumA, sumB);
  printf("\t\tCPU: %4.8f\n\t\tGPU: %4.8f\n", sumCPU, sumC);
  free(a); free(b); free(c);
  cudaFree(ga); cudaFree(gb); cudaFree(gc);
  return(0);
}

int main(int argc, char* argv[])
{
  //matrixmul_CPUvsGPU();
  ex(5, 5);
  printf("\nPress any key to exit.\n");
  getchar();
  return(0);
}