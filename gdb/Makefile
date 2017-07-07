# flags
LDFLAGS = -lpthread
CFLAGS = -Wall -v -H -g -ldl
CC = gcc $(CFLAGS) $(LDFLAGS)

# source
OBJECT = toelinux.o
APPNAME = toelinux

# command
all:	$(APPNAME)
$(APPNAME):	$(OBJECT)
	$(CC) $(OBJECT) -o $(APPNAME)
clean:
	rm -f $(OBJECT) $(APPNAME)