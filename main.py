import string
import sys, time, os, traceback
from random import randint
from numpy import sqrt, power

from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import QThread, pyqtSignal

from paho.mqtt import client as mqtt_client

from datetime import date

import logos_rc

broker = '10.42.0.1'
port = 1883
topic_1 = "esp32/presion"
topic_2 = "esp32/flujo"
client_id = 'Raspberry'

class WorkerThread(QThread):
    
    signal_input = pyqtSignal(str)

    def __init__(self, parent=None):
        QThread.__init__(self)
        
    def run(self):
        while(1):
            client = self.connect_mqtt()
            self.subscribe(client)
            client.loop_forever()

    def connect_mqtt(self) -> mqtt_client:
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print("Connected to MQTT Broker!")
            else:
                print("Failed to connect, return code %d\n", rc)

        client = mqtt_client.Client(client_id)
        #client.username_pw_set(username, password)
        client.on_connect = on_connect
        client.connect(broker, port)
        return client
    
    def subscribe(self,client: mqtt_client):
        def on_message(client, userdata, msg):
            if msg.topic == 'esp32/presion':
                mssg = str(msg.payload.decode())+'p'
                self.signal_input.emit(mssg)
                #print(mssg)
                
            if msg.topic == 'esp32/flujo':
                mssg = str(msg.payload.decode())+'f'
                self.signal_input.emit(mssg)
                
            # mssg = str(msg.payload.decode())
            # self.signal_input.emit(float(mssg))
            
        client.subscribe(topic_1)
        client.subscribe(topic_2)
        #client.subscribe([(topic_1, 0), (topic_2, 0)])
        client.on_message = on_message
    
class Main(QMainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        loadUi('_main_.ui', self)
        
        self.wt=WorkerThread()
        self.wt.start()
        
        self.play_stop_button_.setEnabled(False)
        self.play_stop_button_.clicked.connect(self.play_stop)
        
        self.Vt_pushButton.clicked.connect(self.change)
                
        self.x = list(range(100))  # 100 time points
        
        self.y1 = [0 for i in range(100)]  # 100 data points
        self.y2 = [0 for i in range(100)]  # 100 data points
        self.y3 = [0 for i in range(100)]  # 100 data points
        
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
        self.reinicio_ = 0
        
        self.altura_linedit.setText(self.altura_)
        self.peso_linedit.setText(self.peso_)
        self.sexo_ = self.sexo_linedit.setText('Mujer')
        self.covid_ = self.covid_linedit.setText('No')
        
        self.on_off = 0
        
        today = date.today()
        self.date_label.setText(str(today))
        
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
        if self.reinicio == 1:
            self.apagado_radioButton.setChecked(True)
            self.reinicio = 0
        if index == 1:
            self.altura_label.setText(self.altura_)
            self.peso_label.setText(self.peso_)
            self.sexo_label.setText(self._sexo_)
            self.covid_label.setText(self._covid_)
            
    def encendido(self):
        
        self.on_off_label.setText('Sistema: Encendido')
        
        self.play_stop_button_.setEnabled(True)
        
        self.img_on_off.setPixmap(QtGui.QPixmap("Images/oxygen-mask.jpg"))
        
        pen = pg.mkPen(color=(255, 0, 0))
        pen2 = pg.mkPen(color=(0, 0, 255))
        pen3 = pg.mkPen(color=(0, 128, 0))
        
        self.graphWidget_1.setLabel('bottom', 'Paw')
        self.graphWidget_2.setLabel('bottom', 'Flujo')
        self.graphWidget_3.setLabel('bottom', 'Volumen')
        
        #self.wt.signal_input.connect(self.update_plot_data)
        self.wt.signal_input.connect(self.dato)
        
        self.data_line_1 = self.graphWidget_1.plot(self.x, self.y1, pen=pen)        
        self.data_line_2 = self.graphWidget_2.plot(self.x, self.y2, pen=pen2)
        self.data_line_3 = self.graphWidget_3.plot(self.x, self.y3, pen=pen3)
        
        self.timer = QtCore.QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start() 
        
    def dato(self,value):
        #self.value = float(value)
        if 'p' in value:
            presion = value.replace("p", "")
            self.presion = float(presion)
            
            print('Presion: '+ str(self.presion))
            
        if 'f' in value:
            pre_flujo = value.replace("f", "")
            pre_flujo = float(pre_flujo)
            
            A1=0.000390570
            A2=0.000273472
            RO=1.29
            
            self.flujo = (A1*A2)*(sqrt((2*(pre_flujo*98.0638))/((power(A1,2)-pow(A2,2))*RO)))
            
            print('Flujo: '+ str(self.flujo))

    def apagado(self):
        
        self.on_off_label.setText('Sistema: Apagado')
        
        self.play_stop_button_.setEnabled(False)
        
        self.img_on_off.setPixmap(QtGui.QPixmap("Images/old-man.jpg"))
        self.on_off = 0
        self.graphWidget_1.clear()
        self.graphWidget_2.clear()
        self.graphWidget_3.clear()
        self.timer.stop()    
    
    def reinicio(self):
        self.reinicio_ = 1
        self.tabWidget.setCurrentIndex(0) 
        self.img_on_off.setPixmap(QtGui.QPixmap("Images/old-man.jpg"))
        self.on_off = 0
        self.graphWidget_1.clear()
        self.graphWidget_2.clear()
        self.graphWidget_3.clear()
        self.timer.stop()  
    
    #def update_plot_data(self, dato):
    def update_plot_data(self):
        self.x = self.x[1:]  # Remove the first y element.
        self.x.append(self.x[-1] + 1)  # Add a new value 1 higher than the last.
        #print(dato)
        #self.Vt_label_2.setText(str(dato))
        self.y1 = self.y1[1:]  # Remove the first
        self.y1.append(self.presion)
        #self.y1.append(dato)  # Add a new random value.
        self.y2 = self.y2[1:]  # Remove the first
        self.y2.append(self.flujo)  # Add a new random value.
        self.y3 = self.y3[1:]  # Remove the first
        self.y3.append(randint(0,200))  # Add a new random value.
        
        self.data_line_1.setData(self.x, self.y1)  # Update the data.    
        self.data_line_2.setData(self.x, self.y2)  # Update the data. 
        self.data_line_3.setData(self.x, self.y3)  # Update the data. 
        
    def change(self):
        next_window = Pop(self)
        next_window.show()
              
class Pop(QMainWindow):
    def __init__(self, parent=None):
        super(Pop, self).__init__(parent)
        loadUi('pop_up.ui', self)
        self.slider.valueChanged.connect(self.dato)
        
    def dato(self):
        self.dato_ = str(self.slider.value())
        self.linedit.setText(self.dato_)
        
        
        
  
# #-----------------------------------------------------------------------------------------------------------------#
app = QApplication(sys.argv)
main = Main()
main.show()
sys.exit(app.exec_())