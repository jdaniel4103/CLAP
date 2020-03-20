#!/usr/local/bin/python3.7
import os
import sys
import time

chalnum = sys.argv[1]

try:
	funcarg = sys.argv[2]
except:
	funcarg = ''

names = ['daniel']
times = {}
n = 60

for name in names:
	print('-'*n)
	print('-'*n)
	print('running {}{}.py...'.format(name,chalnum))
	print('-'*n)
	print('script output:')
	filename = name + chalnum + '.py'
	time1 = time.perf_counter()
	os.system('python3 {} {}'.format(filename,funcarg))
	time2 = time.perf_counter()
	runtime = time2 - time1
	times[name] = runtime


print('-'*n)
for name in names:
	print('{}: {} s'.format(name,times[name]))
