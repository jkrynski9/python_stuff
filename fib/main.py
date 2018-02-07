#!/usr/bin/env python3

import sys

def fib(n):
	a,b=0,1
	for i in range(n):
		a,b = b,a+b
		print(a, end=' ')
	print("")

n = int(sys.argv[1])
fib(n)

