/*
liblinux.c
by pioevh@163.com 20170516
*/

#include "liblinux.h"
#include "stdio.h"

int subtract(int a, int b)
{
  return(a - b);
}

int fibonacci(int a)
{
  if (a == 0 || a == 1)
  {
    return(a);
  }
  else
  {
    return(fibonacci(a - 2) + fibonacci(a - 1));
  }
}

int callC()
{
  printf("%d\n", subtract(127, 255));
  printf("%d\n", fibonacci(31));
  return(0);
}
