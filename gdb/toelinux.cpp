/*
toelinux.c
by pioevh@163.com 20170516
*/

#include "stdio.h"
#include "toelinux.hpp"


int hello()
{
  printf("hello!\n");
  return(0);
}


int main()
{
  printf("starting\n");
  hello();
  int a = 1;
  printf("ending %d\n",a);
  scanf("%d", &a);
  return(0);
}
