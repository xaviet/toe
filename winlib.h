/*
libwin.h
by pioevh@163.com 20170516
*/

#pragma once
#ifndef __winlibh__
#define __winlibh__

#include "stdarg.h"
#include "stdio.h"
#include "conio.h"

#define DLLAPI extern "C" __declspec(dllexport)

DLLAPI int __stdcall subtract(int, int);
DLLAPI int __stdcall fibonacci(int);
DLLAPI int __stdcall getCh();

#endif //__winlibh__