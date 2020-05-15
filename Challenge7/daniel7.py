#!/usr/local/bin/python3

import sys
import numpy as np
from configparser import ConfigParser
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from daniel5 import *

class MainWindow(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.setup()

	def setup(self):
		self.setGeometry(0,0,150,200)
		self.setWindowTitle('Dunham Energy')
		self.central_widget = CentralWidget(self)
		self.setCentralWidget(self.central_widget)

		exit_action = QAction('Quit',self)
		exit_action.triggered.connect(qApp.quit)

		menu_bar = self.menuBar()
		menu_bar.setNativeMenuBar(False)
		file_menu = menu_bar.addMenu('File')
		file_menu.addAction(exit_action)

		self.show()

	def closeEvent(self,event):
		reply = QuitMessage().exec_()
		if reply ==QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()

class QuitMessage(QMessageBox):
	def __init__(self):
		QMessageBox.__init__(self)
		self.setText('Are you sure you want to quit?')
		self.addButton(self.No)
		self.addButton(self.Yes)

class CentralWidget(QWidget):
	def __init__(self,parent):
		QWidget.__init__(self,parent)
		self.setup()

	def setup(self):
		self.v1 = 0
		self.J1 = 0
		self.v2 = 0
		self.J2 = 0
		self.E1 = 0.0 # cm^-1
		self.E2 = 0.0 # THz

		self.layout = QGridLayout()

		self.v1_lab = QLabel('v1')
		self.v1_box = QLineEdit(str(self.v1))
		self.layout.addWidget(self.v1_lab,0,0)
		self.layout.addWidget(self.v1_box,0,1)

		self.J1_lab = QLabel('J1')
		self.J1_box = QLineEdit(str(self.J1))
		self.layout.addWidget(self.J1_lab,1,0)
		self.layout.addWidget(self.J1_box,1,1)

		self.v2_lab = QLabel('v2')
		self.v2_box = QLineEdit(str(self.v2))
		self.layout.addWidget(self.v2_lab,2,0)
		self.layout.addWidget(self.v2_box,2,1)

		self.J2_lab = QLabel('J2')
		self.J2_box = QLineEdit(str(self.J2))
		self.layout.addWidget(self.J2_lab,3,0)
		self.layout.addWidget(self.J2_box,3,1)

		self.compute_button = QPushButton('Compute')
		self.compute_button.clicked.connect(self.compute)
		self.layout.addWidget(self.compute_button,4,1)

		self.res_lab = QLabel('E')
		self.res1_box = QLabel(str(self.E1))
		self.res1_unit = QLabel('cm^-1')
		self.res2_box = QLabel(str(self.E2))
		self.res2_unit = QLabel('THz')
		self.layout.addWidget(self.res_lab,5,0)
		self.layout.addWidget(self.res1_box,5,1)
		self.layout.addWidget(self.res1_unit,5,2)
		self.layout.addWidget(self.res2_box,6,1)
		self.layout.addWidget(self.res2_unit,6,2)

		self.setLayout(self.layout)

	def compute(self):
		self.v1 = int(self.v1_box.text())
		self.J1 = int(self.J1_box.text())
		self.v2 = int(self.v2_box.text())
		self.J2 = int(self.J2_box.text())
		state_ids,states = read_in_config()
		Y1 = states['X']['matrix']
		Y2 = states['A']['matrix']
		self.E1 = get_transition_E(Y1,self.v1,self.J1,Y2,self.v2,self.J2)
		self.E2 = wtf(self.E1)
		self.res1_box.setText('{:.4f}'.format(self.E1))
		self.update()
		self.res2_box.setText('{:.6f}'.format(self.E2))
		self.update()


def wtf(wavenumber):
	frequency = wavenumber * 100* 1e-12 * 299792458
	return frequency


if __name__ == '__main__':
	app = QApplication(sys.argv)
	main_window = MainWindow()
	app.exec_()