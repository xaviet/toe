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
  printf("Device : \" %s \" \n\n", prop.name);
  return(_ConvertSMVer2Cores(prop.major, prop.minor) * prop.multiProcessorCount);
}
#endif

#define aW 2
#define aH 2
#define bW 2
#define blocknum 32//32
#define threadnum 256//256

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
  int x;
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
  }
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
      printf("%6f, ", c->element[i*c->width + j]);
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
  const int bid = blockIdx.x;
  const int tid = threadIdx.x;
  int i, x, y;

  for (i = bid * threadnum + tid; i < cw * ch; i += threadnum * blocknum)
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


int main(int argc, char* argv[])
{
  srand(clock());
  int cudaCores = 0;
  if (!(cudaCores=InitCUDA())) {
    return 0;
  }
  //定义矩阵
  //int matrixa[N][N] , matrixb[N][N] , matrixc[N][N] , gpuresult[N][N] , matrixd[N][N] ;
  printf("[%d, %d] * [%d, %d]\n", aW, aH, bW, aW);
  Matrix matrixa = InitMatrix(aW, aH);
  printMatrix(&matrixa, 2, 2);
  Matrix matrixb = InitMatrix(bW, aW);
  printMatrix(&matrixb, 2, 2);
  Matrix matrixc;
  Matrix gpuresult = InitMatrix(bW, aH);

  int matrixprop[6];

  //为CPU运算计时

  //CPU矩阵相乘
  int start = clock();
  matrixc = MM(matrixa, matrixb);
  int finish = clock();
  printMatrix(&matrixc, 4, 4);
  printf("cpu time(single thread)\t\t = %fs %d\n", (float)(finish - start) / CLOCKS_PER_SEC, finish - start);

  SYSTEM_INFO sysInfo;
  GetSystemInfo(&sysInfo);
  start = clock();
  matrixc = multiThreadsMM(matrixa, matrixb, sysInfo.dwNumberOfProcessors);
  finish = clock();
  printf("cpu time(%4d threads)\t\t = %fs %d\n", sysInfo.dwNumberOfProcessors, (float)(finish - start) / CLOCKS_PER_SEC, finish - start);

  start = clock();
  matrixprop[0] = matrixa.width;
  matrixprop[1] = matrixa.height;
  matrixprop[2] = matrixb.width;
  matrixprop[3] = matrixb.height;
  matrixprop[4] = matrixc.width;
  matrixprop[5] = matrixc.height;

  //申请显存
  float *ma, *mb, *mc, *mp;
  cudaMalloc((void**)&ma, sizeof(float) * matrixa.width * matrixa.height);
  cudaMalloc((void**)&mb, sizeof(float) * matrixb.width * matrixb.height);
  cudaMalloc((void**)&mc, sizeof(float) * matrixc.width * matrixc.height);
  cudaMalloc((void**)&mp, sizeof(float) * 6);
  //将数据复制到显存内
  cudaMemcpy(ma, matrixa.element, sizeof(float) * matrixa.width * matrixa.height, cudaMemcpyHostToDevice);
  cudaMemcpy(mb, matrixb.element, sizeof(float) * matrixb.width * matrixb.height, cudaMemcpyHostToDevice);
  cudaMemcpy(mp, matrixprop, sizeof(int) * 6, cudaMemcpyHostToDevice);
  //调用CUDA函数
  MatrixMul <<< blocknum, threadnum, 0 >>>(ma, mb, mc, mp);
  cudaThreadSynchronize();
  //cutilCheckError( cutStopTimer( timer2));
  //将数据从显存中复制出来
  cudaMemcpy(gpuresult.element, mc, sizeof(float) * gpuresult.width * gpuresult.height, cudaMemcpyDeviceToHost);
  finish = clock();
  printf("gpu time(%4d CUDA Cores)\t = %fs %d\n", cudaCores, (float)(finish - start)/CLOCKS_PER_SEC, finish - start);
  printMatrix(&gpuresult, 4, 4);
  for (int i = 0; i < gpuresult.width * gpuresult.height; i++)
  {
    //printf("%d -- %d\n",matrixc.element[ i ],gpuresult.element[ i ]);
    if (matrixc.element[i] != gpuresult.element[i])
    {
      //printf("ERROR");
    }
  }

  cudaFree(ma);
  cudaFree(mb);
  cudaFree(mc);
  cudaFree(mp);

  printf("\nPress any key to exit.\n");
  getchar();

  return 0;
}