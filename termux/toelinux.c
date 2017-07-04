/*
toelinux.c
by pioevh@163.com 20170516
*/

#include "stdio.h"
#include "stdarg.h"
#include "toelinux.h"
#include "py.h"

int main()
{
  printf("%d %d\n",subtract(1,3),fibonacci(31));
  pyOpen();
  printf("fibonacci %d subtract %d\n", pyFunction("commonlib", "fibonacci", "(i)", 31), pyFunction("commonlib", "subtract", "(ii)", 127, 255));
  pyClose();
  return(0);
}
