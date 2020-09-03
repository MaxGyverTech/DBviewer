# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\MaxGyver\Documents\VS code\pyapps\firstapp\UIs\linePlCombo.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(278, 97)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(200, 0))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.txt1 = QtWidgets.QLabel(self.centralwidget)
        self.txt1.setObjectName("txt1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.txt1)
        self.edittxt = QtWidgets.QLineEdit(self.centralwidget)
        self.edittxt.setObjectName("edittxt")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.edittxt)
        self.txt2 = QtWidgets.QLabel(self.centralwidget)
        self.txt2.setObjectName("txt2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.txt2)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.confBtn = QtWidgets.QPushButton(self.centralwidget)
        self.confBtn.setObjectName("confBtn")
        self.horizontalLayout.addWidget(self.confBtn)
        self.cansBtn = QtWidgets.QPushButton(self.centralwidget)
        self.cansBtn.setObjectName("cansBtn")
        self.horizontalLayout.addWidget(self.cansBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.txt1.setText(_translate("MainWindow", "TextLabel"))
        self.txt2.setText(_translate("MainWindow", "TextLabel"))
        self.confBtn.setText(_translate("MainWindow", "Создать поле"))
        self.cansBtn.setText(_translate("MainWindow", "Отмена"))
