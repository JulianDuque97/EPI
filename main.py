import sys, time, os, traceback
from random import randint

from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from PyQt5 import QtGui
from PyQt5 import QtCore

import logos_rc
#-----------------------------------------------------------------------------------------------------------------#
#GUI
class Datos_paciente_(QMainWindow):
    def __init__(self, parent=None):
        super(Datos_paciente_, self).__init__(parent)
        loadUi('Datos_paciente.ui', self)
        self.altura_linedit.editingFinished.connect(self.dato_altura)
        self.peso_linedit.editingFinished.connect(self.dato_peso)
        self.sexo_linedit.editingFinished.connect(self.dato_sexo)
        self.covid_linedit.editingFinished.connect(self.dato_covid)
        self.siguiente_button.clicked.connect(self.siguiente)
        
    def dato_altura(self):
        self.altura = self.altura_linedit.text()
        #self.altura_linedit.setEnabled(False)
        return self.altura
            
    def dato_peso(self):
        self.peso = self.peso_linedit.text()
        #self.peso_linedit.setEnabled(False)
        return self.peso
    
    def dato_sexo(self):
        self.sexo = self.sexo_linedit.text()
        #self.sexo_linedit.setEnabled(False)
        return self.sexo
    
    def dato_covid(self):
        self.covid = self.covid_linedit.text()
        #self.covid_linedit.setEnabled(False)
        return self.covid
            
    def siguiente(self):
        self.close()
        previous_window = MyApp(self)
        previous_window.show()
        	
class MyApp(Datos_paciente_):
    
    def __init__(self,  Datos_paciente_):
        super(MyApp, self).__init__(Datos_paciente_)
        loadUi('main.ui', self)
        # self.ON.setEnabled(True)
        # self.OFF.setEnabled(False)
        # self.play_stop_button_.setEnabled(False)
        # self.variable_button_.toggle()
        # self.ON.clicked.connect(self.btn_on)
        # self.OFF.clicked.connect(self.btn_off)
        # self.play_stop_button_.clicked.connect(self.play_stop)
        # self.datos_button_.clicked.connect(self.datos_paciente)
        # self.variable_button_.clicked.connect(self.variables_paciente)
                        
        self.on_off = 0
        
        #self.label_27.setStyleSheet("color:rgb(0, 0, 0);")
                                
        self.x = list(range(100))  # 100 time points
        
        self.y1 = [randint(0,100) for _ in range(100)]  # 100 data points
        self.y2 = [randint(0,100) for _ in range(100)]  # 100 data points
        self.y3 = [randint(0,100) for _ in range(100)]  # 100 data points

        self.graphWidget_7.setBackground('w')    
        self.graphWidget_8.setBackground('w')
        self.graphWidget_9.setBackground('w')
        
    def play_stop(self):
        
        if self.on_off == 1:
            self.on_off = 0
            self.timer.start()
        else:
            self.on_off = 1
            self.timer.stop()    
    
    def datos_paciente(self):
        #self.hide()
        next_window = Pop_up(self)
        next_window.show()
        
    def variables_paciente(self):
        
        next_window = Variables_paciente(self)
        next_window.show()                       
    
    def update_plot_data(self):
        self.x = self.x[1:]  # Remove the first y element.
        self.x.append(self.x[-1] + 1)  # Add a new value 1 higher than the last.
        
        self.y1 = self.y1[1:]  # Remove the first
        self.y1.append(randint(0,100))  # Add a new random value.
        self.y2 = self.y2[1:]  # Remove the first
        self.y2.append(randint(0,200))  # Add a new random value.
        self.y3 = self.y3[1:]  # Remove the first
        self.y3.append(randint(0,200))  # Add a new random value.
        
        self.Ppeak_label.setText(str(self.y1[-1]))
        self.label_29.setText(str(self.y1[-1]))
        self.label_32.setText(str(self.y1[-1]))
        self.label_35.setText(str(self.y1[-1]))
        
        self.data_line_1.setData(self.x, self.y1)  # Update the data.    
        self.data_line_2.setData(self.x, self.y2)  # Update the data. 
        self.data_line_3.setData(self.x, self.y3)  # Update the data.    
        
    def btn_on(self):
        
        self.play_stop_button.setEnabled(True)
        self.img_on_off.setPixmap(QtGui.QPixmap("Images/oxygen-mask.jpg"))
        self.lb_on_off.setText("System: On")
        self.on.setEnabled(False)
        self.off.setEnabled(True)
        
        pen = pg.mkPen(color=(255, 0, 0))
        pen2 = pg.mkPen(color=(0, 0, 255))
        pen3 = pg.mkPen(color=(0, 128, 0))
        self.data_line_1 =  self.graphWidget_1.plot(self.x, self.y1, pen=pen)        
        self.data_line_2 =  self.graphWidget_2.plot(self.x, self.y2, pen=pen2)
        self.data_line_3 =  self.graphWidget_3.plot(self.x, self.y2, pen=pen3)
        
        self.timer = QtCore.QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()
                               
    def btn_off(self):
        self.play_stop_button.setEnabled(False)
        self.img_on_off.setPixmap(QtGui.QPixmap("Images/old-man.jpg"))
        self.lb_on_off.setText("System: Off")
        self.on.setEnabled(True)
        self.off.setEnabled(False)
        self.on_off = 0
        self.graphWidget_1.clear()
        self.graphWidget_2.clear()
        self.graphWidget_3.clear()
        self.timer.stop()     
        
    def close_window(self):
        return self.close()
    
class Pop_up(QMainWindow):
    def __init__(self, parent=None):
        super(Pop_up, self).__init__(parent)
        loadUi('Pop_up.ui', self)
        self.close_window_ = MyApp.close_window(self)
        self.regresar.clicked.connect(self.Regresar)
        self.continuar.clicked.connect(self.Continuar)
    def Regresar(self):
        if self.regresar.isChecked():
            self.close()
    def Continuar(self): 
        if self.continuar.isChecked():
            self.close()
            self.close_window_
            next_window = Datos_paciente_(self)
            next_window.show()
            
            
        
        
class Variables_paciente(MyApp):
    def __init__(self, MyApp):
        super(Variables_paciente, self).__init__(MyApp)
        loadUi('Variables.ui', self)
        self.back_button.clicked.connect(self.back)
        #self.dato_altura_ = Datos_paciente_.dato_altura(self)
        # self.altura_label.setText(self.dato_altura)
        
    def back(self):
        self.close()
         

        
#-----------------------------------------------------------------------------------------------------------------#
app = QApplication(sys.argv)
main = Datos_paciente_()
main.show()
sys.exit(app.exec_())