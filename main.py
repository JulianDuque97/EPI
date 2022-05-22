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
class Datos_paciente(QMainWindow):
    def __init__(self, parent=None):
        super(Datos_paciente, self).__init__(parent)
        loadUi('Datos_paciente.ui', self)
        self.altura_linedit.editingFinished.connect(self.datos)
        self.peso_linedit.editingFinished.connect(self.datos)
        self.sexo_linedit.editingFinished.connect(self.datos)
        self.covid_linedit.editingFinished.connect(self.datos)
        self.siguiente_button.clicked.connect(self.siguiente)
        
    def datos(self):
        self.altura = self.altura_linedit.text()
        self.peso = self.peso_linedit.text()
        self.sexo = self.sexo_linedit.text()
        self.covid = self.covid_linedit.text()
        
    def siguiente(self):
        self.close()
        previous_window = Pop_up_1(self)
        previous_window.show()	
        
class Pop_up_1(QMainWindow):
    def __init__(self, parent=None):
        super(Pop_up_1, self).__init__(parent)
        loadUi('pop_up_1.ui', self)
        self.ok_button.clicked.connect(self.siguiente)
        
    def siguiente(self):
        self.close()
        next_window = MyApp(self)
        next_window.show()
    
    def close_(self):
        self.close()

class MyApp(QMainWindow):
    
    def __init__(self, parent=None):
        super(MyApp, self).__init__(parent)
        loadUi('main.ui', self)
        self.on.setEnabled(True)
        self.off.setEnabled(False)
        self.play_stop_button.setEnabled(False)
        self.variable_button.toggle()
        self.on.clicked.connect(self.btn_on)
        self.off.clicked.connect(self.btn_off)
        self.play_stop_button.clicked.connect(self.play_stop)
        self.datos_button.clicked.connect(self.datos_paciente)
        self.variable_button.clicked.connect(self.variables_paciente)
        
        self.on_off = 0
                                
        self.x = list(range(100))  # 100 time points
        
        self.y1 = [randint(0,100) for _ in range(100)]  # 100 data points
        self.y2 = [randint(0,100) for _ in range(100)]  # 100 data points
        self.y3 = [randint(0,100) for _ in range(100)]  # 100 data points

        self.graphWidget_1.setBackground('w')    
        self.graphWidget_2.setBackground('w')
        self.graphWidget_3.setBackground('w')
        
    def play_stop(self):
        
        if self.on_off == 1:
            self.on_off = 0
            self.timer.start()
        else:
            self.on_off = 1
            self.timer.stop()    
    
    def datos_paciente(self):
        next_window = Pop_up_2(self)
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

class Pop_up_2(MyApp):
    def __init__(self, MyApp):
        super(Pop_up_2, self).__init__(MyApp)
        loadUi('pop_up_2.ui', self)
        self.no_button.clicked.connect(self.no)
        self.si_button.clicked.connect(self.si)
        
    def no(self):
        self.close()
                             
    def si(self):
        self.close()
        main.show()
        
                 
class Variables_paciente(QMainWindow):
    def __init__(self, parent=None):
        super(Variables_paciente, self).__init__(parent)
        loadUi('Variables.ui', self)
        self.back_button.clicked.connect(self.siguiente)
        
    def siguiente(self):
        self.close()
        # previous_window = MyApp(self)
        # previous_window.show()
#-----------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------#
app = QApplication(sys.argv)
main = Datos_paciente()
main.show()
sys.exit(app.exec_())