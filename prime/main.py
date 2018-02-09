#!/usr/bin/env python3

import sys

def prime(n):
	c = 0
	for a in range(2,n):
		for x in range(2,a):
			if a % x == 0:
				break
		else:
			if c < 10:
				print(a, end='\t')
				c += 1
			else:
				c = 1
				print()
				print(a, end='\t')


print("Prime numbers to ", sys.argv[1])
prime(int(sys.argv[1]))
print()

