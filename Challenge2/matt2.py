i = 3
seqpos = 1
holder = 0

print('Type a Positive Integer please: ' )
number = input()

while True:
	if int(number) == 1:
		seqpos = 0
		break

	if int(number) == 2 or 3:
		seqpos = seqpos
		break	

	holder = seqpos
	seqpos = seqpos + holder		
	i = i + 1

	if i == int(number):
		print(seqpos)
		break


more = input ()