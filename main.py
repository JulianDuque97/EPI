import sys, time, os, traceback
from random import randint

from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
from PyQt5 import uic, QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

qtcreator_file  = "UI.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)

#-----------------------------------------------------------------------------------------------------------------#
#Thread

#-----------------------------------------------------------------------------------------------------------------#
#GUI
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
                
        self.on.setEnabled(True)
        self.off.setEnabled(False)
        self.on.toggle()
        self.off.toggle()
        self.systems.toggle()
        self.on.clicked.connect(self.btn_on)
        self.off.clicked.connect(self.btn_off)
                        
        self.x = list(range(100))  # 100 time points
        self.y = [randint(0,100) for _ in range(100)]  # 100 data points
        
        self.y2 = [randint(0,100) for _ in range(100)]  # 100 data points

        self.graphWidget.setBackground('w')    
                    
    def update_plot_data(self):
        self.x = self.x[1:]  # Remove the first y element.
        self.x.append(self.x[-1] + 1)  # Add a new value 1 higher than the last.
        self.y = self.y[1:]  # Remove the first
        self.y.append(randint(0,100))  # Add a new random value.
        
        self.y2 = self.y2[1:]  # Remove the first
        self.y2.append(randint(0,200))  # Add a new random value.
        
        self.Ppeak.setText(str(self.y[-1]))
        self.label_29.setText(str(self.y[-1]))
        self.label_32.setText(str(self.y[-1]))
        self.label_35.setText(str(self.y[-1]))
        
        self.data_line_1.setData(self.x, self.y)  # Update the data.    
        self.data_line_2.setData(self.x, self.y2)  # Update the data.    
        
    def btn_on(self):
        self.img_on_off.setPixmap(QtGui.QPixmap("Images/oxygen-mask.jpg"))
        self.lb_on_off.setText("System: On")
        self.on.setEnabled(False)
        self.off.setEnabled(True)
        
        pen = pg.mkPen(color=(255, 0, 0))
        pen2 = pg.mkPen(color=(0, 0, 255))
        self.data_line_1 =  self.graphWidget.plot(self.x, self.y, pen=pen)        
        self.data_line_2 =  self.graphWidget.plot(self.x, self.y2, pen=pen2)
        
        self.timer = QtCore.QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()
                               
    def btn_off(self):
        self.img_on_off.setPixmap(QtGui.QPixmap("Images/old-man.jpg"))
        self.lb_on_off.setText("System: Off")
        self.on.setEnabled(True)
        self.off.setEnabled(False)
        
        self.graphWidget.clear()
        self.timer.stop()     
        
#-----------------------------------------------------------------------------------------------------------------#
#This is the function that works as Thread    

    
#-----------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------#
app = QtWidgets.QApplication(sys.argv)
window = MyApp()
window.show()
sys.exit(app.exec_())