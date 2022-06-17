import sys, time, os, traceback
from random import randint

from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from PyQt5 import QtGui
from PyQt5 import QtCore

import logos_rc

class main(QMainWindow):
    def __init__(self, parent=None):
        super(main, self).__init__(parent)
        loadUi('_main_.ui', self)
        
        #self.tabWidget.setCurrentIndex(2)
        
        self.play_stop_button_.setEnabled(False)
        self.play_stop_button_.clicked.connect(self.play_stop)
                
        self.x = list(range(100))  # 100 time points
        
        self.y1 = [randint(0,100) for _ in range(100)]  # 100 data points
        self.y2 = [randint(0,100) for _ in range(100)]  # 100 data points
        self.y3 = [randint(0,100) for _ in range(100)]  # 100 data points
        
        self.graphWidget_1.setBackground('w')    
        self.graphWidget_2.setBackground('w')
        self.graphWidget_3.setBackground('w')
        
        self.altura_linedit.setReadOnly(True)
        self.peso_linedit.setReadOnly(True)
        self.sexo_linedit.setReadOnly(True)
        self.covid_linedit.setReadOnly(True)
        
        self.tabWidget.currentChanged.connect(self.tabs)
        self.altura_slider.valueChanged.connect(self.altura)
        self.peso_slider.valueChanged.connect(self.peso)
        self.sexo_slider.valueChanged.connect(self.sexo)
        self.covid_slider.valueChanged.connect(self.covid)
        
        self.encendido_radioButton.toggled.connect(self.encendido)
        self.apagado_radioButton.toggled.connect(self.apagado)
        self.reiniciar_radioButton.toggled.connect(self.reinicio)
        
        self.altura_ = '140'
        self.peso_ = '40'
        self._sexo_ = 'Hombre'
        self._covid_ = 'No'
        
        self.altura_linedit.setText(self.altura_)
        self.peso_linedit.setText(self.peso_)
        self.sexo_ = self.sexo_linedit.setText('Mujer')
        self.covid_ = self.covid_linedit.setText('No')
        
        self.on_off = 0
        
    def play_stop(self):
        if self.on_off == 1:
            self.on_off = 0
            self.play_stop_button_.setText('Stop')
            self.timer.start()
        else:
            self.on_off = 1
            self.play_stop_button_.setText('Play')
            self.timer.stop()
        
    def altura(self):
        self.altura_ = str(self.altura_slider.value())
        self.altura_linedit.setText(self.altura_)
        
    def peso(self):
        self.peso_ = str(self.peso_slider.value())
        self.peso_linedit.setText(self.peso_)

    def sexo(self):
        self.sexo_ = self.sexo_slider.value()
        if self.sexo_ == 1:
            self._sexo_ = 'Hombre'
            self.sexo_linedit.setText(self._sexo_)
        else:
            self._sexo_ = 'Mujer'
            self.sexo_linedit.setText(self._sexo_)
  
    def covid(self):
        self.covid_ = self.covid_slider.value()
        if self.covid_ == 1:
            self._covid_ = 'Si'
            self.covid_linedit.setText(self._covid_)
        else:
            self._covid_ = 'No'
            self.covid_linedit.setText(self._covid_)
        
    def tabs(self):
        index = self.tabWidget.currentIndex()
        if index == 2:
            self.altura_label.setText(self.altura_)
            self.peso_label.setText(self.peso_)
            self.sexo_label.setText(self._sexo_)
            self.covid_label.setText(self._covid_)
            
    def encendido(self):
        self.play_stop_button_.setEnabled(True)
        
        self.img_on_off.setPixmap(QtGui.QPixmap("Images/oxygen-mask.jpg"))
        
        pen = pg.mkPen(color=(255, 0, 0))
        pen2 = pg.mkPen(color=(0, 0, 255))
        pen3 = pg.mkPen(color=(0, 128, 0))
        self.data_line_1 = self.graphWidget_1.plot(self.x, self.y1, pen=pen)        
        self.data_line_2 = self.graphWidget_2.plot(self.x, self.y2, pen=pen2)
        self.data_line_3 = self.graphWidget_3.plot(self.x, self.y3, pen=pen3)
        
        self.timer = QtCore.QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start() 
    
    def apagado(self):
        
        self.play_stop_button_.setEnabled(False)
        
        self.img_on_off.setPixmap(QtGui.QPixmap("Images/old-man.jpg"))
        self.on_off = 0
        self.graphWidget_1.clear()
        self.graphWidget_2.clear()
        self.graphWidget_3.clear()
        self.timer.stop()    
    
    def reinicio(self):
        pass 
    
    def update_plot_data(self):
        self.x = self.x[1:]  # Remove the first y element.
        self.x.append(self.x[-1] + 1)  # Add a new value 1 higher than the last.
        
        self.y1 = self.y1[1:]  # Remove the first
        self.y1.append(randint(0,100))  # Add a new random value.
        self.y2 = self.y2[1:]  # Remove the first
        self.y2.append(randint(0,50))  # Add a new random value.
        self.y3 = self.y3[1:]  # Remove the first
        self.y3.append(randint(0,200))  # Add a new random value.
        
        self.data_line_1.setData(self.x, self.y1)  # Update the data.    
        self.data_line_2.setData(self.x, self.y2)  # Update the data. 
        self.data_line_3.setData(self.x, self.y3)  # Update the data. 
  
# #-----------------------------------------------------------------------------------------------------------------#
app = QApplication(sys.argv)
main = main()
main.show()
sys.exit(app.exec_())