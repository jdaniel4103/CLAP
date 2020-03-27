i = 0
seqpos = 1
holder = 0

print('Type a Positive Integer please: ' )
number = input()

while True:
	if number == 1:
		seqpos = 0
		break
	holder = seqpos
	seqpos = seqpos + holder		
	i = i + 1
	print('nice')		
	if i == number:
		break


print('goodjob!')

print(seqpos)

more = input ()