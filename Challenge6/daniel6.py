import numpy as np
from configparser import ConfigParser
import matplotlib.pyplot as plt

class branch():
	def __init__(self,branch,v1,v2):
		self.branch = branch
		self.v1 = v1
		self.v2 = v2
		self.n = 10
		self.lines = self.get_lines()

	def get_lines(self):
		lines = []
		for i in range(self.n):
			if self.branch == 'Q': # deltaJ = 0
				lower_state = state('X',self.v1,i)
				upper_state = state('A',self.v2,i)
			elif self.branch == 'P': # deltaJ = -1
				lower_state = state('X',self.v1,i+1)
				upper_state = state('A',self.v2,i)
			elif self.branch == 'R': # deltaJ = +1
				lower_state = state('X',self.v1,i)
				upper_state = state('A',self.v2,i+1)
			else:
				print('BAD BRANCH')

			lines.append(line(lower_state,upper_state))
		return lines


class line():
	def __init__(self,state_1,state_2):
		self.s1 = state_1
		self.s2 = state_2
		self.E = np.abs(self.s2.E - self.s1.E)
		self.T = 4 # K
		self.a = self.get_amp()

	def get_amp(self):
		kb = 1.38064852e-23 # m^2*kg*s^-2*K^-1
		h = 6.62607004e-34 # m^2*kg*s^-1
		c = 299792458

		B = 2.4393006612e-1 # cm^-1
		we = 481.774655196 # cm^-1

		J = self.s1.J
		Ej = h*c*100*B*J*(J+1)
		Q_rot = kb*self.T/(h*c*100*B)
		A_rot = (2*J + 1)*np.exp(-Ej/(kb*self.T))/Q_rot

		v = self.s1.v
		Ev = h*c*we*(v + 1/2)
		stf = h*c*we/(kb*self.T)
		Q_vib = ((1 - np.exp(-stf))**-1)*np.exp(-stf/2) 
		A_vib = np.exp(-Ev/(kb*self.T))/Q_vib

		FCF = 1

		return A_rot*A_vib*FCF

	def get_f(self,num):
		f = np.linspace(-num,num,1000)*1e-6 + self.E
		return f

	def get_A(self):
		f = self.get_f(500)
		kb = 1.38064852e-23 # m^2*kg*s^-2*K^-1
		amu = 1.6605402e-27 # kg/amu
		m = 62 * amu # kg, AlCl mass
		c = 299792458 # m/s, speed of light
		sigma = np.sqrt(kb*self.T/(m*c**2))*self.E
		A = self.a/(sigma*np.sqrt(2*np.pi)) # Scale factor for Gaussian
		Abs = A*np.exp(-(f-self.E)**2/(2*sigma**2)) # Doppler broadened line
		return Abs, f


class state():
	def __init__(self,el,v,J):
		self.el = el
		self.v = v
		self.J = J
		self.E = self.set_E()

	def set_E(self):
		state_ids,states = read_in_config()
		self.Y = states[self.el]['matrix']
		new_E = 0.0
		for i in range(np.shape(self.Y)[0]):
			for j in range(3):
				new_E += self.Y[i][j] * ((self.v + 0.5)**i) * ((self.J * (self.J + 1))**j)

		return wtf(new_E)



def wtf(wavenumber):
	frequency = wavenumber * 100* 1e-12 * 299792458
	return frequency


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
	X00 = state('X',0,0)
	A00 = state('A',0,0)
	print('\nX v=0 J=0 Energy (THz):',X00.E)
	print('A v=0 J=0 Energy (THz):',A00.E)

	line1 = line(X00,A00)
	print('\nLine Energy for X,v=0,J=0 -> A,v=0,J=0 (THz):',line1.E)
	data,fs = line1.get_A()
	plt.figure()
	plt.plot((fs-line1.E)*1e6,data)
	plt.xlabel('MHz from {} THz'.format(line1.E))
	plt.ylabel('Absorption (arb.)')
	plt.title('Plot of Doppler-broadened Line at {}'.format(line1.E))

	Q00 = branch('Q',0,0)
	P00 = branch('P',0,0)
	R00 = branch('R',0,0)
	Q11 = branch('Q',1,1)
	P11 = branch('P',1,1)
	R11 = branch('R',1,1)
	print('\nFirst Q00 Line Energy (THz):',Q00.lines[0].E)
	print('First P00 Line Energy (THz):',P00.lines[0].E)

	plt.figure()
	for lin in Q00.lines:
		new_data,new_fs = lin.get_A()
		plt.plot(new_fs,new_data,'r')
	for lin in P00.lines:
		new_data,new_fs = lin.get_A()
		plt.plot(new_fs,new_data,'b')
	for lin in R00.lines:
		new_data,new_fs = lin.get_A()
		plt.plot(new_fs,new_data,'g')
	for lin in Q11.lines:
		new_data,new_fs = lin.get_A()
		plt.plot(new_fs,new_data,'r')
	for lin in P11.lines:
		new_data,new_fs = lin.get_A()
		plt.plot(new_fs,new_data,'b')
	for lin in R11.lines:
		new_data,new_fs = lin.get_A()
		plt.plot(new_fs,new_data,'g')
	plt.xlabel('Frequency (THz)')
	plt.ylabel('Absorption (arb.)')
	plt.title('Sample P/Q/R (Blue/Red/Green) Branches')

	plt.show()

