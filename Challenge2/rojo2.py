# Tristan Rojo
# Challenge 2: Fibonacci USA (via System Arguments)
# The script takes an integer system argument (n); prints the list of n numbers and the nth value in the Fibonacci Sequence  


# Comments: Only error-proof in negative integers

import sys

def fibonacci(num): # say n = 20

    if num == 1:
        return 1
    
    elif num == 2:
        return 1
    
    else:
        n1 = 1
        n2 = 1
        
        list = []
        list.append(n1)
        list.append(n2)
        
        for i in range(num-2):
            nth = n2 + n1
            list.append(nth)
            temp = n2
            n2 = nth
            n1 = temp
  	
    print (list)	
    return (list[num-1])
        


if len(sys.argv) == 2: 

    n = sys.argv[1]

    while (int(n)<=0):

        n = (input('Enter a Positive Integer:'))
        
              
        
    print ('The', str(n) +'th value:', fibonacci(int(n)))

else: 
    print ("***No input from sys.argv[1]")
    print ()

    n = input("Enter a Positive Integer: ")

    while (int(n)<=0):

        n = (input('Enter a Positive Integer:'))
        
              
        
    print ('The', str(n) +'th value:', fibonacci(int(n)))


