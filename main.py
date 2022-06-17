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
        pass 
    
    def apagado(self):
        pass 
    
    def reinicio(self):
        pass 
  
# #-----------------------------------------------------------------------------------------------------------------#
app = QApplication(sys.argv)
main = main()
main.show()
sys.exit(app.exec_())