# Challenge 2: Fibonacci USA (Using System Arguments)

Due: Mar 27, 2020

The purpose of this challenge is to learn how to use system arguments when calling a python function.  A standard python call is "python3 script.py" ("py script.py" in Windows), however if you need to change a parameter in script.py everytime you run it, then it makes sense to utilize system arguments.  These arguments typically look like "python3 script.py arg", where "arg" is the argument that will be read in by the function.  An example we use regularly in lab is in our simple data display script call.  An example call would be "python3 plot_alcl 123456" where 123456 represents the time of a frequency scan in HHMMSS format.

## Challenge Tasks:

1. Read up on how to use the python feature "sys.argv".
2. Write a script that:
	1. Takes in a positive integer as an argument.
	2. Prints out that number in the Fibonacci sequence.
	3. Example: if the argument is 20, print the 20th value in the Fibonacci sequence.