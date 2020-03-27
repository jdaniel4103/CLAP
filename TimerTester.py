#!/usr/local/bin/python3.7
import os
import sys
import time

chalnum = sys.argv[1]
scriptpath = '/Users/johnr/Documents/Github/CLAP/Challenge{}/'.format(chalnum)
testpath = '/Users/johnr/Desktop/'

try:
	funcarg = sys.argv[2]
except:
	funcarg = ''

names = ['daniel','rojo']
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
	os.system('cd {};python3 {} {}'.format(scriptpath,filename,funcarg))
	time2 = time.perf_counter()
	runtime = time2 - time1
	times[name] = runtime


print('-'*n)
for name in names:
	print('{}: {} s'.format(name,times[name]))
