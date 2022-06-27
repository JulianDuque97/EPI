from statistics import variance
import string
import sys, time, os, traceback
from tkinter import Variable
from random import randint
from numpy import sqrt, power, var

from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import QThread, pyqtSignal

from paho.mqtt import client as mqtt_client
import paho.mqtt.client as mqtt

from datetime import date

import logos_rc

broker = '10.42.0.1'
port = 1883
topic_1 = "esp32/presion"
topic_2 = "esp32/flujo"
topic_3 = 'esp32/volumen'
topic_4 = 'esp32/pagina_web'
client_id = 'Raspberry'
client = mqtt_client.Client(client_id)

opcion = ''
valor_Vt = 0

class WorkerThread(QThread):
    
    signal_input = pyqtSignal(str)

    def __init__(self, parent=None):
        QThread.__init__(self)
        
    def run(self):
        while(1):
            try:
                client = self.connect_mqtt()
                self.subscribe(client)
            except os.error:
                print("not connected to network")
                self.signal_input.emit("1")
            

    def connect_mqtt(self):
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print("Connected to MQTT Broker!")
                self.signal_input.emit("0")
        def on_disconnect(client, userdata, rc):
            if rc != 0:
                print("Unexpected MQTT disconnection. Will auto-reconnect")
                self.signal_input.emit("1")
        
        client.on_connect = on_connect
        client.on_disconnect = on_disconnect
        client.connect(broker, port)
        client.loop_forever()
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
        client.subscribe(topic_4)
        #client.subscribe([(topic_1, 0), (topic_2, 0)])
        client.on_message = on_message
    
class Main(QMainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        loadUi('_main_.ui', self)
        
        client.publish(topic_3, '0')
        
        self.wt=WorkerThread()
        self.wt.start()
        
        self.timer = QtCore.QTimer()
        
        self.wt.signal_input.connect(self.dato)
        
        self.play_stop_button_.setEnabled(False)
        self.Vt_slider.setEnabled(False)
        self.play_stop_button_.clicked.connect(self.play_stop)
                               
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
        self.detener_radioButton.toggled.connect(self.detener)
        self.reiniciar_radioButton.toggled.connect(self.reinicio)
                
        self.Vt_slider.valueChanged.connect(self.change_Vt)
        
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
        
    def change_Vt(self):
        value_Vt = self.Vt_slider.value()
    
        if value_Vt == 0:
            self.posicion_motor = '0'
            self.Vt_label.setText('0')
            self.Vt_label_2.setText('0')
            client.publish(topic_3, self.posicion_motor)
           
        elif value_Vt == 1:
            self.posicion_motor = '3'
            self.Vt_label.setText('138')
            self.Vt_label_2.setText('138')
            client.publish(topic_3, self.posicion_motor)
            
        elif value_Vt == 2:
            self.posicion_motor = '4'
            self.Vt_label.setText('191.5')
            self.Vt_label_2.setText('191.5')
            client.publish(topic_3, self.posicion_motor)
            
        elif value_Vt == 3:
            self.posicion_motor = '5'
            self.Vt_label.setText('252')
            self.Vt_label_2.setText('252')
            client.publish(topic_3, self.posicion_motor)
        
        elif value_Vt == 4:
            self.posicion_motor = '6'
            self.Vt_label.setText('316.7')
            self.Vt_label_2.setText('316.7')
            client.publish(topic_3, self.posicion_motor)
            
        elif value_Vt == 5:
            self.posicion_motor = '7'
            self.Vt_label.setText('378.1')
            self.Vt_label_2.setText('378.1')
            client.publish(topic_3, self.posicion_motor)
            
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
        if self.reinicio_ == 1:
            self.detener_radioButton.setChecked(True)
            self.reinicio_ = 0
        if index == 1:
            
            self.altura_label.setText(self.altura_)
            self.peso_label.setText(self.peso_)
            self.sexo_label.setText(self._sexo_)
            self.covid_label.setText(self._covid_)
            
    def encendido(self):
        self.graphWidget_1.clear()
        self.graphWidget_2.clear()
        self.graphWidget_3.clear()
        self.on_off_label.setText('Sistema: Encendido')
        self.encendido_radioButton.setText("Encendido")
        self.detener_radioButton.setText("Detener")
        self.play_stop_button_.setEnabled(True)
        self.Vt_slider.setEnabled(True)          
        self.img_on_off.setPixmap(QtGui.QPixmap("Images/oxygen-mask.jpg"))
        #COLOR GRAFICAS    
        pen = pg.mkPen(color=(255, 0, 0))
        pen2 = pg.mkPen(color=(0, 0, 255))
        pen3 = pg.mkPen(color=(0, 128, 0))
        #LABELS GRAFICAS
        self.graphWidget_1.setLabel('bottom', 'Paw')
        self.graphWidget_2.setLabel('bottom', 'Flujo')
        self.graphWidget_3.setLabel('bottom', 'Volumen')
        #ACTIVANDO THREAD
        #self.wt.signal_input.connect(self.update_plot_data)
        self.wt.signal_input.connect(self.dato)
        #PASANDO X,Y & COLORES A LA GRAFICA
        self.data_line_1 = self.graphWidget_1.plot(self.x, self.y1, pen=pen)        
        self.data_line_2 = self.graphWidget_2.plot(self.x, self.y2, pen=pen2)
        self.data_line_3 = self.graphWidget_3.plot(self.x, self.y3, pen=pen3)
        #ACTIVANDO EL TIMER, SE PUEDE CAMBIAR EL TIEMPO DE MUESTREO PARA LAS GRAFICAS
        #self.timer.timeout.connect(self.update_plot_data)
        self.timer.setInterval(100)
        self.timer.start()
        
    def dato(self,value):
        if 'p' in value:
            presion = value.replace("p", "")
            self.presion = float(presion)
            print('Presion: '+ str(self.presion))
            
        if 'f' in value:
            pre_flujo = value.replace("f", "")
            self.flujo = float(pre_flujo)
            print('Flujo: '+ str(self.flujo))
            
        if '1' in value:
            self.label.setStyleSheet("background-color: rgb(255, 0, 0)")
            self.label.setText("NOT CONNECTED")
            
        elif '0' in value:
            self.label.setStyleSheet("background-color: rgb(51, 209, 122)")
            self.label.setText("CONNECTED")
                    
    def detener(self):
        self.on_off_label.setText('Sistema: Detenido')
        self.encendido_radioButton.setText("Encender")
        self.detener_radioButton.setText("Detenido")
        self.play_stop_button_.setEnabled(False)
        self.Vt_slider.setEnabled(False)
        self.img_on_off.setPixmap(QtGui.QPixmap("Images/old-man.jpg"))
        self.on_off = 0
        client.publish(topic_3, '0')
    
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
        
    # def change_Vt(self):
    #     global opcion
    #     opcion = 'Vt'
    #     next_window = Pop(self)
    #     next_window.show()
              
# class Pop(QMainWindow):
#     def __init__(self, parent=None):
#         super(Pop, self).__init__(parent)
#         loadUi('pop_up.ui', self)
#         self.slider.valueChanged.connect(self.dato)
                
#     def dato(self):
#         if opcion == 'Vt':
#             global valor_Vt
#             self.slider.setMinimum(0)
#             self.slider.setMaximum(7)
#             self.value = self.slider.value()
#             if self.value == 0:
#                 valor_Vt = 0
#                 self.linedit.setText(str(valor_Vt) + ' ml')
#             elif self.value == 1:
#                 valor_Vt = 138
#                 self.linedit.setText(str(valor_Vt) +' ml')
            
            
# #-----------------------------------------------------------------------------------------------------------------#
app = QApplication(sys.argv)
main = Main()
main.show()
sys.exit(app.exec_())