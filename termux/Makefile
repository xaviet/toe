# lib flags
LIBLDFLAGS = -ldl 
LIBCFLAGS = -Wall -v -g -shared -fPIC
LIBCC = gcc $(LIBCFLAGS) $(LIBLDFLAGS)
LIBCREATE = ar crs
LIBOUTPATH = ./output/
# lib source
LIBNAME = liblinux
LIBOBJECT = $(LIBNAME).o
DLLNAME = $(LIBOUTPATH)$(LIBNAME).so
SLLNAME = $(LIBOUTPATH)$(LIBNAME).a 


# app flags
SYSTEMPATH = /data/data/com.termux/files/usr/
LDFLAGS = -lpthread -ldl -L$(SYSTEMPATH)lib -lpython3.6m
CFLAGS = -Wall -v -g -I../commonlib -I$(SYSTEMPATH)include/python3.6m
EXTLIB = -L./output -l:$(LIBNAME).a
CC = gcc $(CFLAGS) $(LDFLAGS)
# app source
APPNAME = toelinux
APPOBJECT = $(APPNAME).o


# command
lib:	$(DLLNAME)
$(DLLNAME):	$(LIBOBJECT)
	$(LIBCC) $(LIBOBJECT) -o $(DLLNAME)
	$(LIBCREATE) $(SLLNAME) $(LIBOBJECT)


app:	$(APPNAME)
$(APPNAME):	$(APPOBJECT)
	$(CC) $(APPOBJECT) -o $(APPNAME) $(EXTLIB)


clean:
	rm -f $(LIBOBJECT) $(DLLNAME) $(SLLNAME) $(APPNAME) $(APPOBJECT)
