/*
libwin.cpp
by pioevh@163.com 20170516
*/

#include "winlib.h"

DLLAPI int __stdcall subtract(int a, int b)
{
  return(a - b);
}

DLLAPI int __stdcall fibonacci(int a)
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

DLLAPI int __stdcall getCh()
{
  return(_getch());
}