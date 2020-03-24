# John Daniel
# Challenge 2: Fibonacci USA (Using System Arguments)
# This script takes in an integer system argument (n) and prints the nth number in the Fibonacci sequence.

import sys

def fibnum(num):
	if num == 1:
		return 1
	elif num == 2:
		return 1
	else:
		return fibnum(num-1) + fibnum(num-2)

num_to_fib = int(sys.argv[1])

print(fibnum(num_to_fib))