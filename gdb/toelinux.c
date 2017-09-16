/*
toelinux.c
by pioevh@163.com 20170516
*/

#include "stdio.h"
#include "toelinux.h"
#include "interfacepasslib.h"

int hello()
{
  printf("hello!\n");
  return(0);
}


int main(int argc, char** argv)
{
  printf("starting\n");
  hello();
  int a = 1;
  printf("ending %d\n", a);
  scanf("%d", &a);
  printf("ending %d\n", a);
  //maintest(argc, argv);
  return(0);
}
