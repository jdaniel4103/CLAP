#Tristan Rojo
#Challenge %
#Role:

import numpy as np
from configparser import ConfigParser
import sys
import time

def config_parse():

	config = ConfigParser()
	config.read('line_config.ini')

	energy_level = config.sections() # X and A.
	energy_lvl_dict = {} # Our Dictionary contains X and A

	#config.section - returns a list of sections available
	#config.options - returns a list of options available in the specified section
	#config.get - gets the fallback values; get an option value for the names section

	#For each state in energy level:
		#Read the Values - config.options
		#Create a List for the specified Energy Level
			#Dictionary:
				# X = [y00,y01,y02,...,] 
				# A = [y00,y01,y02,...,]
		# Do this by Dictionaries. Grouping of Lists with Dictionaries
		# Why Dictionaries: Holds a key:value pair. Lists holds only one per

	for energy_id in energy_level: #energy_id: X,A
		list1 = [0.0,0.0,0.0]
		list2 = [0.0,0.0,0.0]
		list3 = [0.0,0.0,0.0]
		value_matrix = ([list1,list2,list3])

		energy_lvl_dict[energy_id] = {} # Grouping by Dictionaries

		for key in config.options(energy_id): #Y00,Y01,Y02,...
			value = np.float(config.get(energy_id,key)) #gets value from key
			energy_lvl_dict[energy_id][key] = value
			key_id = list(key) 
			value_matrix[int(key_id[1])][int(key_id[2])] = value #access mth row and nth column by the args inside and put a value in it
			energy_lvl_dict[energy_id][' '] = value_matrix

	print (energy_lvl_dict , sep= '\n')
	print ()
	print ()


	time.sleep (2)


	return energy_level, energy_lvl_dict

	
def energy(Y,vib,rot): # a need two for-loops needed (matrix needed)
	Energy = 0.0
	for i in range(3):
		for j in range(3):
			Energy += Y[i][j] * ((vib + 0.5)**i) * ((rot * (rot + 1))**j)

	return Energy


def transition(Y1,v_vib_1st,J_rot_1st,Y2,v_vib_2nd,J_rot_2nd):

	Former_Energy = energy(Y1,v_vib_1st,J_rot_1st)
	Latter_Energy = energy(Y2,v_vib_2nd,J_rot_2nd)
	Transition_Value = Latter_Energy - Former_Energy 

	return Transition_Value



def main():

	#We will go from X -> A transition
	#We need to calculate the energy in the given transition


	v_vib_1st = int(sys.argv[1])
	J_rot_1st = int(sys.argv[2])
	v_vib_2nd = int(sys.argv[3])
	J_rot_2nd = int(sys.argv[4])

	while v_vib_2nd > 2 or v_vib_1st > 2 or v_vib_2nd < 0 or v_vib_1st < 0:
		print (" Please Enter 0,1,2 for vibrational lvl")
		v_vib_1st = int(input('v_vib_1st:'))
		v_vib_2nd = int(input('v_vib_2nd'))

	while J_rot_2nd > 2 or J_rot_1st > 2 or J_rot_2nd < 0 or J_rot_1st < 0:
		print (" Please Enter 0,1,2 for rotational lvl")
		J_rot_1st = int(input('J_rot_1st:'))
		J_rot_2nd = int(input('J_rot_2nd'))	 

	energy_level, energy_lvl_dict = config_parse()


	print ('1st Vibrational State =', v_vib_1st)
	print ('1st Rotational State =', J_rot_1st)
	print ('2nd Vibrational State =', v_vib_2nd)
	print ('2nd Rotational State =', J_rot_2nd)

	time.sleep (2)

	Y1 = energy_lvl_dict['X'][' ']
	Y2 = energy_lvl_dict['A'][' ']

	final= transition(Y1,v_vib_1st,J_rot_1st,Y2,v_vib_2nd,J_rot_2nd)

	print ('Transition Energy =',final)

if __name__ == '__main__':
    main()