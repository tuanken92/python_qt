# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\python_tut\python_gui\ex1\calculator_gui.ui',
# licensing of 'D:\python_tut\python_gui\ex1\calculator_gui.ui' applies.
#
# Created: Tue May 28 22:28:32 2019
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(268, 209)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.edtA = QtWidgets.QLineEdit(self.centralwidget)
        self.edtA.setGeometry(QtCore.QRect(110, 30, 113, 21))
        self.edtA.setObjectName("edtA")
        self.edtB = QtWidgets.QLineEdit(self.centralwidget)
        self.edtB.setGeometry(QtCore.QRect(110, 70, 113, 21))
        self.edtB.setObjectName("edtB")
        self.btnSum = QtWidgets.QPushButton(self.centralwidget)
        self.btnSum.setGeometry(QtCore.QRect(40, 110, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.btnSum.setFont(font)
        self.btnSum.setStyleSheet("background-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.btnSum.setObjectName("btnSum")
        self.lbResult = QtWidgets.QLabel(self.centralwidget)
        self.lbResult.setGeometry(QtCore.QRect(120, 110, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.lbResult.setFont(font)
        self.lbResult.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: rgb(85, 170, 255);")
        self.lbResult.setAlignment(QtCore.Qt.AlignCenter)
        self.lbResult.setObjectName("lbResult")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 30, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"color: rgb(0, 0, 127);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 70, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"color: rgb(0, 0, 127);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 268, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.btnSum.setText(QtWidgets.QApplication.translate("MainWindow", "Sum A+B", None, -1))
        self.lbResult.setText(QtWidgets.QApplication.translate("MainWindow", "SUM", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "Number A", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "Number B", None, -1))

