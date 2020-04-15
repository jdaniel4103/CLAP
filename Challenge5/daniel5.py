# Challenge 5
# John Daniel
# This script takes vibrational and rotational quantum numbers for the X and A state of AlCl and returns the energy using the Dunham expansion.

import numpy as np
from configparser import ConfigParser
import sys

def get_state_E(Y,v,J):
	# Dunham Expansion
	E = 0.0
	for i in range(3):
		for j in range(3):
			E += Y[i][j] * ((v + 0.5)**i) * ((J * (J + 1))**j)

	return E


def get_transition_E(Y1,v1,J1,Y2,v2,J2):
	# Difference between state energies (transition energy)
	return (get_state_E(Y2,v2,J2) - get_state_E(Y1,v1,J1))


def read_in_config(filename = 'line_config.ini'):

	config = ConfigParser() # creates config object
	config.read(filename) # reads in file
	state_ids = config.sections() # gets sections names
	states = {}

	for state in state_ids:
		coeff_mat = np.zeros((3,3))
		coeffs = config.options(state) # gets coefficient names i.e. 'y10'
		states[state] = {}
		for coeff in coeffs:
			new_coeff = np.float(config.get(state,coeff)) # gets coefficient value
			states[state][coeff] = new_coeff
			name_list = list(coeff) # splits coefficient name in to list i.e. ['y','1','0']
			coeff_mat[int(name_list[1]),int(name_list[2])] = new_coeff
		states[state]['matrix'] = coeff_mat

	return state_ids,states


if __name__ == '__main__':
	v1 = int(sys.argv[1])
	J1 = int(sys.argv[2])
	v2 = int(sys.argv[3])
	J2 = int(sys.argv[4])

	print('Energy for X -> A transition for:')
	print('v\' = {}'.format(v1))
	print('J\' = {}'.format(J1))
	print('v\" = {}'.format(v2))
	print('J\" = {}'.format(J2))

	state_ids,states = read_in_config()

	Y1 = states['X']['matrix']
	Y2 = states['A']['matrix']

	deltaJ = J2 - J1
	deltav = v2 - v1
	if np.abs(deltaJ) > 1:
		print('FORBIDDEN TRANSITION!!!')
		print('delta J = {}'.format(deltaJ))
	if np.abs(deltav) > 1:
		print('FORBIDDEN TRANSITION!!!')
		print('delta v = {}'.format(deltav))

	energy = get_transition_E(Y1,v1,J1,Y2,v2,J2)
	print('Transition Energy: {}'.format(energy))

