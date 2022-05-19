# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Documents\Projects\EPI\Datos_paciente.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1046, 757)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logos/Images/heart-monitoring.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(76, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(470, 280))
        self.frame.setStyleSheet("QFrame{\n"
"image: url(:/logos/Images/conversation.png);\n"
"}\n"
"QLabel{\n"
"image:none;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(120, 40, 231, 141))
        font = QtGui.QFont()
        font.setFamily("LEMON MILK")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.frame)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(312, 320))
        self.label.setStyleSheet("image: url(:/logos/Images/ventilation.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout_4, 1, 1, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(322, 450))
        self.frame_2.setMaximumSize(QtCore.QSize(290, 550))
        self.frame_2.setStyleSheet("QFrame{\n"
"border:2px solid rgb(0, 0, 0);\n"
"\n"
"border-radius: 50px;\n"
"background-color: rgb(129, 61, 156);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QLabel{\n"
"border: 2px sold rgb(255, 255, 255)\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 0, 0, 5, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 85, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem3, 0, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem4, 2, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(18, -1, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.altura_linedit = QtWidgets.QLineEdit(self.frame_2)
        self.altura_linedit.setMinimumSize(QtCore.QSize(200, 50))
        self.altura_linedit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("LEMON MILK")
        font.setPointSize(12)
        self.altura_linedit.setFont(font)
        self.altura_linedit.setStyleSheet("QLineEdit{\n"
"border:2px solid rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"color: #FFF;\n"
"background-color:rgb(34,36,44);\n"
"\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"border: 2px sold rgb(255, 255, 255)\n"
"\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border:2px solid rgb(85, 170, 255);\n"
"background-color: rgb(45, 45, 56);\n"
"}")
        self.altura_linedit.setInputMask("")
        self.altura_linedit.setText("")
        self.altura_linedit.setAlignment(QtCore.Qt.AlignCenter)
        self.altura_linedit.setClearButtonEnabled(False)
        self.altura_linedit.setObjectName("altura_linedit")
        self.verticalLayout_2.addWidget(self.altura_linedit)
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("LEMON MILK")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(166, 166, 166);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.peso_linedit = QtWidgets.QLineEdit(self.frame_2)
        self.peso_linedit.setMinimumSize(QtCore.QSize(200, 50))
        self.peso_linedit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("LEMON MILK")
        font.setPointSize(12)
        self.peso_linedit.setFont(font)
        self.peso_linedit.setStyleSheet("QLineEdit{\n"
"border:2px solid rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"color: #FFF;\n"
"background-color:rgb(34,36,44);\n"
"\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"border: 2px sold rgb(255, 255, 255)\n"
"\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border:2px solid rgb(85, 170, 255);\n"
"background-color: rgb(45, 45, 56);\n"
"}")
        self.peso_linedit.setInputMask("")
        self.peso_linedit.setText("")
        self.peso_linedit.setAlignment(QtCore.Qt.AlignCenter)
        self.peso_linedit.setClearButtonEnabled(False)
        self.peso_linedit.setObjectName("peso_linedit")
        self.verticalLayout_2.addWidget(self.peso_linedit)
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("LEMON MILK")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(166, 166, 166);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.sexo_linedit = QtWidgets.QLineEdit(self.frame_2)
        self.sexo_linedit.setMinimumSize(QtCore.QSize(200, 50))
        self.sexo_linedit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("LEMON MILK")
        font.setPointSize(12)
        self.sexo_linedit.setFont(font)
        self.sexo_linedit.setStyleSheet("QLineEdit{\n"
"border:2px solid rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"color: #FFF;\n"
"background-color:rgb(34,36,44);\n"
"\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"border: 2px sold rgb(255, 255, 255)\n"
"\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border:2px solid rgb(85, 170, 255);\n"
"background-color: rgb(45, 45, 56);\n"
"}")
        self.sexo_linedit.setInputMask("")
        self.sexo_linedit.setText("")
        self.sexo_linedit.setAlignment(QtCore.Qt.AlignCenter)
        self.sexo_linedit.setClearButtonEnabled(False)
        self.sexo_linedit.setObjectName("sexo_linedit")
        self.verticalLayout_2.addWidget(self.sexo_linedit)
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("LEMON MILK")
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(166, 166, 166);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.covid_linedit = QtWidgets.QLineEdit(self.frame_2)
        self.covid_linedit.setMinimumSize(QtCore.QSize(200, 50))
        self.covid_linedit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("LEMON MILK")
        font.setPointSize(12)
        self.covid_linedit.setFont(font)
        self.covid_linedit.setStyleSheet("QLineEdit{\n"
"border:2px solid rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"color: #FFF;\n"
"background-color:rgb(34,36,44);\n"
"\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"border: 2px sold rgb(255, 255, 255)\n"
"\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border:2px solid rgb(85, 170, 255);\n"
"background-color: rgb(45, 45, 56);\n"
"}")
        self.covid_linedit.setInputMask("")
        self.covid_linedit.setText("")
        self.covid_linedit.setAlignment(QtCore.Qt.AlignCenter)
        self.covid_linedit.setClearButtonEnabled(False)
        self.covid_linedit.setObjectName("covid_linedit")
        self.verticalLayout_2.addWidget(self.covid_linedit)
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("LEMON MILK")
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(166, 166, 166);")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 3, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 127, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem5, 4, 1, 1, 1)
        self.label_44 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("LEMON MILK")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_44.setFont(font)
        self.label_44.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_44.setStyleSheet("QLabel{\n"
"border: 2px sold rgb(255, 255, 255)\n"
"}")
        self.label_44.setAlignment(QtCore.Qt.AlignCenter)
        self.label_44.setObjectName("label_44")
        self.gridLayout_3.addWidget(self.label_44, 1, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem6, 0, 3, 5, 1)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.siguiente_button = QtWidgets.QPushButton(self.centralwidget)
        self.siguiente_button.setMinimumSize(QtCore.QSize(140, 45))
        self.siguiente_button.setMaximumSize(QtCore.QSize(140, 45))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.siguiente_button.setFont(font)
        self.siguiente_button.setStyleSheet("QPushButton{\n"
"    color: rgb(247, 247, 247);\n"
"    background-color: rgb(51, 209, 122);\n"
"    border-radius: 10%;\n"
"    border: 1px solid #000;\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover {background-color: rgb(230, 97, 0);}\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"  border: 1.5px solid black;\n"
"}")
        self.siguiente_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/logos/Images/right-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.siguiente_button.setIcon(icon1)
        self.siguiente_button.setIconSize(QtCore.QSize(45, 45))
        self.siguiente_button.setCheckable(True)
        self.siguiente_button.setObjectName("siguiente_button")
        self.horizontalLayout.addWidget(self.siguiente_button)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem8)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 3, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem9, 0, 1, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem10, 1, 2, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem11, 1, 4, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem12, 2, 1, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem13, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ventilador mecanico"))
        self.label_3.setText(_translate("MainWindow", "Hola!,\n"
"Antes de comenzar, no se te olvide ingresar los siguientes datos."))
        self.altura_linedit.setPlaceholderText(_translate("MainWindow", "Altura"))
        self.label_4.setText(_translate("MainWindow", "Altura en cm"))
        self.peso_linedit.setPlaceholderText(_translate("MainWindow", "Peso"))
        self.label_5.setText(_translate("MainWindow", "Peso en kg"))
        self.sexo_linedit.setPlaceholderText(_translate("MainWindow", "Sexo"))
        self.label_6.setText(_translate("MainWindow", "Sexo"))
        self.covid_linedit.setPlaceholderText(_translate("MainWindow", "Covid"))
        self.label_7.setText(_translate("MainWindow", "Tiene covid el paciente?"))
        self.label_44.setText(_translate("MainWindow", "Datos del paciente"))
import logos_rc
