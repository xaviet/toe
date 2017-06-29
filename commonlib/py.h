/*
py.h
by pioevh@163.com 20170517
*/

#ifndef __pyh__
#define __pyh__

#include "Python.h"
#include "stdarg.h"

int pyOpen()
{
  Py_Initialize();
  PyRun_SimpleString("import sys");
  PyRun_SimpleString("import os");
  PyRun_SimpleString("sys.path.append('..{0}commonlib'.format(os.sep))");
  return(0);
}

int pyAddPath(const char* string)
{
  PyRun_SimpleString(string);
  return(0);
}

int pyFunction(const char* module, const char* function, const char* format, ...)
{
  PyObject *pModule, *pFunc, *pParameter, *pRetVal;
  int rt = 0;
  pModule = PyImport_ImportModule(module);
  pFunc = PyObject_GetAttrString(pModule, function);
  va_list vargs;
  va_start(vargs, format);
  pParameter = Py_VaBuildValue(format, vargs);
  va_end(vargs);
  pRetVal = PyEval_CallObject(pFunc, pParameter);
  PyArg_Parse(pRetVal, "i", &rt);
  Py_DECREF(pRetVal);
  Py_DECREF(pParameter);
  Py_DECREF(pFunc);
  Py_DECREF(pModule);
  return(rt);
}

int pyClose()
{
  Py_Finalize();
  return(0);
}

#endif //__pyh__