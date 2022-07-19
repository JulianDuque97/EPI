from statistics import variance
import string
import sys, time, os, traceback
from tkinter import Variable
from random import randint
import numpy as np

from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot

from paho.mqtt import client as mqtt_client
import paho.mqtt.client as mqtt

from datetime import date

import logos_rc

broker = '10.42.0.1'
port = 1883
topic_1 = "esp32/presion"
topic_2 = "esp32/flujo"
topic_3 = 'esp32/volumen'
topic_4 = 'esp32/ti'
topic_5 = 'esp32/volumen_tidal'
topic_6 = 'esp32/setpoint'
topic_7 = 'esp32/kp'
topic_8 = 'esp32/ki'
topic_9 = 'esp32/kd'
client_id = 'Raspberry'
client = mqtt_client.Client(client_id)

valor_Vt = 0

presion_average = []

class WorkerThread(QThread):

    signal_input = pyqtSignal(str)

    def __init__(self, parent=None):
        QThread.__init__(self)

    def run(self):
        while(1):
            try:
                client = self.connect_mqtt()
                self.subscribe(client)
                client.loop_forever()
            except os.error:
                #print("not connected to network")
                self.signal_input.emit("1")

    def connect_mqtt(self):
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                self.signal_input.emit("0")
                #print("Connected to MQTT Broker!")

        def on_disconnect(client, userdata, rc):
            if rc != 0:
                self.signal_input.emit("1")
                #print("Unexpected MQTT disconnection. Will auto-reconnect")

        client.on_connect = on_connect
        client.on_disconnect = on_disconnect
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
                #print(mssg)

            # mssg = str(msg.payload.decode())
            # self.signal_input.emit(float(mssg))

        client.subscribe(topic_1)
        client.subscribe(topic_2)
        client.subscribe(topic_4)
        client.subscribe(topic_5)
        client.subscribe(topic_6)
        client.subscribe(topic_7)
        client.subscribe(topic_8)
        client.subscribe(topic_9)
        client.on_message = on_message

class Main(QMainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        loadUi('_main_.ui', self)

        self.wt=WorkerThread()
        self.wt.start()
        client.publish(topic_3, '0')

        self.posicion_motor = '0'
        self.ppeak = 0
        self.pflujo = 0
        self.valor_2 = 0
        self.tct = 0
        self.flujo = 0
        self.timer = QtCore.QTimer()

        self.wt.signal_input.connect(self.banner)

        self.play_stop_button_.setEnabled(False)
        self.grafica_button.setEnabled(False)
        self.Vt_slider.setEnabled(False)
        self.Ti_slider.setEnabled(False)
        self.kp_lineEdit.setEnabled(False)
        self.ki_lineEdit.setEnabled(False)
        self.kd_lineEdit.setEnabled(False)
        self.play_stop_button_.clicked.connect(self.play_stop)
        self.grafica_button.clicked.connect(self.grafica)

        self.x = list(range(100))  # 100 time points

        self.y1 = [0 for i in range(100)]  # 100 data points
        self.y2 = [0 for i in range(100)]  # 100 data points
        self.y3 = [0 for i in range(100)]  # 100 data points

        self.graphWidget_1.setBackground('w')
        self.graphWidget_2.setBackground('w')
        self.graphWidget_3.setBackground('w')

        self.graphWidget_1.show()
        self.graphWidget_2.hide()
        self.graphWidget_3.hide()

        self.checkBox.toggled.connect(self.encendido_apagado)

        self.Vt_slider.valueChanged.connect(self.change_Vt)
        self.Ti_slider.valueChanged.connect(self.change_Ti)

        self.kp_lineEdit.editingFinished.connect(self.control_kp)
        self.ki_lineEdit.editingFinished.connect(self.control_ki)
        self.kd_lineEdit.editingFinished.connect(self.control_kd)

        self.on_off = 0

        today = date.today()
        self.date_label.setText(str(today))

    def control_kp(self):
        client.publish(topic_7, str(self.kp_lineEdit.text()))

    def control_ki(self):
        client.publish(topic_8, str(self.ki_lineEdit.text()))

    def control_kd(self):
        client.publish(topic_9, str(self.kd_lineEdit.text()))

    def change_Ti(self):
        value_Ti = self.Ti_slider.value()
        if value_Ti == 0:
            self.Ti_label.setText('0')
            self.Ti_label_.setText('0')
        elif value_Ti == 1:
            self.Ti_label.setText('0.6')
            self.Ti_label_.setText('0.6')
        elif value_Ti == 2:
            self.Ti_label.setText('0.7')
            self.Ti_label_.setText('0.7')
        elif value_Ti == 3:
            self.Ti_label.setText('0.8')
            self.Ti_label_.setText('0.8')
        elif value_Ti == 4:
            self.Ti_label.setText('0.9')
            self.Ti_label_.setText('0.9')
        elif value_Ti == 5:
            self.Ti_label.setText('1.0')
            self.Ti_label_.setText('1.0')
        elif value_Ti == 6:
            self.Ti_label.setText('1.1')
            self.Ti_label_.setText('1.1')
        elif value_Ti == 7:
            self.Ti_label.setText('1.2')
            self.Ti_label_.setText('1.2')
        elif value_Ti == 8:
            self.Ti_label.setText('1.3')
            self.Ti_label_.setText('1.3')
        elif value_Ti == 9:
            self.Ti_label.setText('1.4')
            self.Ti_label_.setText('1.4')
        elif value_Ti == 10:
            self.Ti_label.setText('1.5')
            self.Ti_label_.setText('1.5')
        self.Value_Ti = self.Ti_label.text()
        self.Value_Ti = float(self.Value_Ti)
        client.publish(topic_4, self.Value_Ti)
        Value_Te = self.Value_Ti*2
        self.Te_label.setText(str(Value_Te))
        self.Te_label_2.setText(str(Value_Te))
        self.tct = self.Value_Ti + Value_Te

        Ti = float(self.Ti_label.text())/60
        Vt = float(self.Vt_label.text())*(1/1000)
        if Ti>0:
            set_point = Vt/Ti
            set_point = round(set_point, 2)
            self.SetU_label.setText(str(set_point))
            self.SetU_label_2.setText(str(set_point))
            fr = 60/((float(self.Ti_label.text()))+(float(self.Ti_label.text())*2))
            fr = round(fr,2)
            self.f_label.setText(str(fr))
            self.f_label_2.setText(str(fr))
            client.publish(topic_6, str(set_point))
        else:
            set_point = 0
            self.SetU_label.setText('0')
            self.SetU_label_2.setText('0')
            client.publish(topic_6, str(set_point))

    def banner(self,value):
        if value == '1':
            self.label.setStyleSheet("background-color: rgb(255, 0, 0)")
            self.label.setText("NOT CONNECTED")
        if value == '0':
            self.label.setStyleSheet("background-color: rgb(51, 209, 122)")
            self.label.setText("CONNECTED")

    def change_Vt(self):
        value_Vt = self.Vt_slider.value()
        if value_Vt == 0:
            self.posicion_motor = '0'
            self.U_label.setText('0')
            self.U_label_2.setText('0')
            self.Vt_label.setText('0')
            self.Vt_label_2.setText('0')
            self.presion_label.setText('0')
            #client.publish(topic_3, self.posicion_motor)

        elif value_Vt == 1:
            self.ppeak = 0
            self.posicion_motor = '3'
            self.Vt_label.setText('138')
            self.Vt_label_2.setText('138')
            #client.publish(topic_3, self.posicion_motor)

        elif value_Vt == 2:
            self.ppeak = 0
            self.posicion_motor = '4'
            self.Vt_label.setText('191.5')
            self.Vt_label_2.setText('191.5')
            #client.publish(topic_3, self.posicion_motor)

        elif value_Vt == 3:
            self.ppeak = 0
            self.posicion_motor = '5'
            self.Vt_label.setText('252')
            self.Vt_label_2.setText('252')
            #client.publish(topic_3, self.posicion_motor)

        elif value_Vt == 4:
            self.ppeak = 0
            self.posicion_motor = '6'
            self.Vt_label.setText('316.7')
            self.Vt_label_2.setText('316.7')
            #client.publish(topic_3, self.posicion_motor)

        elif value_Vt == 5:
            self.ppeak = 0
            self.posicion_motor = '7'
            self.Vt_label.setText('378.1')
            self.Vt_label_2.setText('378.1')
            #client.publish(topic_3, self.posicion_motor)

        client.publish(topic_3, self.posicion_motor)

    def play_stop(self):
        if self.on_off == 1:
            self.on_off = 0
            self.play_stop_button_.setText('Stop')
            client.publish(topic_3, self.posicion_motor)
            self.Vt_slider.setEnabled(True)
            self.Ti_slider.setEnabled(True)
            self.kp_lineEdit.setEnabled(True)
            self.ki_lineEdit.setEnabled(True)
            self.kd_lineEdit.setEnabled(True)
            self.timer.start()
        else:
            self.on_off = 1
            client.publish(topic_3, '0')
            self.play_stop_button_.setText('Play')
            self.Vt_slider.setEnabled(False)
            self.Ti_slider.setEnabled(False)
            self.kp_lineEdit.setEnabled(False)
            self.ki_lineEdit.setEnabled(False)
            self.kd_lineEdit.setEnabled(False)
            self.timer.stop()

    def encendido_apagado(self):
        self.checkBox.setEnabled(False)
        self.Ti_slider.setEnabled(True)
        self.kp_lineEdit.setEnabled(True)
        self.ki_lineEdit.setEnabled(True)
        self.kd_lineEdit.setEnabled(True)
        self.presion_label.setText('0')
        self.U_label.setText('0')
        self.U_label_2.setText('0')
        if self.checkBox.isChecked() == True:
            self.grafica_ = 1
            client.publish(topic_3, self.posicion_motor)
            self.graphWidget_1.clear()
            self.graphWidget_2.clear()
            self.graphWidget_3.clear()
            self.on_off_label.setText('Sistema: Encendido')
            self.checkBox.setText("Encendido")
            self.play_stop_button_.setEnabled(True)
            self.grafica_button.setEnabled(True)
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
            self.timer.timeout.connect(self.update_plot_data)
            self.timer.setInterval(100)
            self.timer.start()

        else:
            self.checkBox.setText("Apagado")
            client.publish(topic_3, '0')
            self.on_off = 0
            self.graphWidget_1.clear()
            self.graphWidget_2.clear()
            self.graphWidget_3.clear()
            self.on_off_label.setText('Sistema: Apagado')
            self.play_stop_button_.setEnabled(False)
            self.Vt_slider.setEnabled(False)
            self.img_on_off.setPixmap(QtGui.QPixmap("Images/old-man.jpg"))

    def dato(self,value):
        if 'p' in value:
            presion = value.replace("p", "")
            presion = float(presion)
            #presion = (((presion)* 0.8056640625)/3.2359)/10;
            presion = round(presion,2)
            if presion < 0.99:
                self.presion = 0
            else:
                self.presion = presion

            if self.ppeak < self.presion:
                self.presion_label.setText(str(self.presion))
                self.pip_label.setText(str(self.presion))
                self.U_label.setText(str(self.flujo))
                self.U_label_2.setText(str(self.flujo))
                self.ppeak = self.presion

        if 'f' in value:
            flujo = value.replace("f", "")
            flujo = float(flujo)
            if flujo> 30:
                self.flujo = 30
            else:
                self.flujo = flujo

        if self.valor_2 <= self.tct:
            self.valor_1 = self.tct * 0.01
            self.valor_2 = self.valor_1
            self.volumen = self.flujo*self.valor_2
            self.volumen = self.volumen*1000
            self.valor_2 = self.valor_2+self.valor_1
            client.publish(topic_5, str(self.volumen))

    def grafica(self):
        if self.grafica_ == 1:
            self.grafica_ = 2
            self.grafica_button.setText('Flujo')
            self.graphWidget_1.hide()
            self.graphWidget_2.show()
            self.graphWidget_3.hide()
        elif self.grafica_ == 2:
            self.grafica_ = 0
            self.grafica_button.setText('Volumen')
            self.graphWidget_1.hide()
            self.graphWidget_2.hide()
            self.graphWidget_3.show()
        elif self.grafica_ == 0:
            self.grafica_ = 1
            self.grafica_button.setText('Presion')
            self.graphWidget_1.show()
            self.graphWidget_2.hide()
            self.graphWidget_3.hide()

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
        #self.y3.append(randint(0,200))  # Add a new random value.
        self.y3.append(self.volumen)  # Add a new random value.

        self.data_line_1.setData(self.x, self.y1)  # Update the data.
        self.data_line_2.setData(self.x, self.y2)  # Update the data.
        self.data_line_3.setData(self.x, self.y3)  # Update the data.

# #-----------------------------------------------------------------------------------------------------------------#
app = QApplication(sys.argv)
main = Main()
main.show()
sys.exit(app.exec_())