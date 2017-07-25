/*
py.h
by pioevh@163.com 20170725
*/


#include "stdio.h"
#include "stdlib.h"


int main()
{
  unsigned int size=512*1024*1024-1;
  char* p1=NULL;
  char* p2=NULL;
  char* p3=NULL;
  char* p4=NULL;
  p1=(char*)malloc(size);
  p2=(char*)malloc(size);
  p3=(char*)malloc(size);
  p4=(char*)malloc(size);
  for(unsigned int i=0;i<size;i++)
  {
    *(p1+i)=i;
    *(p2+i)=i;
    *(p3+i)=i;
    *(p4+i)=i;
  }
  for(unsigned int i=0;i<size;i++)
  {
    if((*(p1+i)!=*(p2+i))&&(*(p1+i)!=*(p3+i))&&(*(p1+i)!=*(p4+i)))
    {
      printf("fault:%d\n",i);
    }
  }
  return(0);  
}
