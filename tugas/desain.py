import sys, os, glob
from PyQt4 import QtCore, QtGui, uic
import serial, time

qtCreatorFile = "desain.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

#global ser
#ser = serial.Serial("COM6", "9600", timeout=0.1)

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		Ui_MainWindow.__init__(self)
		self.setupUi(self)
		self.pushButton_OpenSerial.clicked.connect(self.OpenSerial)
		self.toolButton_on.clicked.connect(self.On)
		self.pushButton_Exit.clicked.connect(self.AppExit)
		self.toolButton_off.clicked.connect(self.Off)
		
	def OpenSerial(self):
		if self.pushButton_OpenSerial.text()=='Open Serial':
			self.ser = serial.Serial("COM6", "9600", timeout=0.1)

		
	def On(self):
		self.ser.write('x'.encode())
	def Off(self):
		self.ser.write('c'.encode())	

	def AppExit(self):
		sys.exit()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
