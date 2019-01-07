CC = gcc
PYVERSION=3.5
FLAGS = -shared -pthread -fPIC -fwrapv -O2 -Wall -fno-strict-aliasing -I/usr/include/python${PYVERSION} -o

default: compile clean

compile:
	cython mod_funcs.pyx
	${CC} ${FLAGS} mod_funcs.so mod_funcs.c

clean:
	rm mod_funcs.c

