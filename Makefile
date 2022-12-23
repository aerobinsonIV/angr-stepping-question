all:
	gcc -g -gdwarf-4 binary.c -o binary -O2 -Wno-unused-result