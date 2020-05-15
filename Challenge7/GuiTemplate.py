#!/usr/local/bin/python3

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.setup()

	def setup(self):
		self.setGeometry(0,0,800,600)
		self.setWindowTitle('Main Window')
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
		pass







if __name__ == '__main__':
	app = QApplication(sys.argv)
	main_window = MainWindow()
	app.exec_()