import sys

i = 3
holder = 1
seqpos = 1

print('Type a Positive Integer please: ' )
number = int(sys.argv[1])

if number == 1:
		seqpos = 0

if number == 2 or 3:
	seqpos = seqpos

if number > 3:
	while number != i:

		seqpos = seqpos + holder		
		i = i + 1
		holder = seqpos - holder

print(seqpos)

more = input ()