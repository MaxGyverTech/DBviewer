# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\MaxGyver\Documents\VS code\pyapps\firstapp\UIs\new_table.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(412, 307)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.tableNameE = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableNameE.setFont(font)
        self.tableNameE.setObjectName("tableNameE")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.tableNameE)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.newWriteBtn = QtWidgets.QPushButton(self.centralwidget)
        self.newWriteBtn.setObjectName("newWriteBtn")
        self.verticalLayout.addWidget(self.newWriteBtn)
        self.delWriteBtn = QtWidgets.QPushButton(self.centralwidget)
        self.delWriteBtn.setObjectName("delWriteBtn")
        self.verticalLayout.addWidget(self.delWriteBtn)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.LabelRole, self.verticalLayout)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.listWidget)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.createBtn = QtWidgets.QPushButton(self.centralwidget)
        self.createBtn.setMinimumSize(QtCore.QSize(80, 0))
        self.createBtn.setObjectName("createBtn")
        self.horizontalLayout.addWidget(self.createBtn)
        self.cansBtn = QtWidgets.QPushButton(self.centralwidget)
        self.cansBtn.setMinimumSize(QtCore.QSize(80, 0))
        self.cansBtn.setObjectName("cansBtn")
        self.horizontalLayout.addWidget(self.cansBtn)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Создать таблицу(beta)"))
        self.label_2.setText(_translate("MainWindow", "Название таблицы"))
        self.label_3.setText(_translate("MainWindow", "Структура"))
        self.newWriteBtn.setText(_translate("MainWindow", "+ поле"))
        self.delWriteBtn.setText(_translate("MainWindow", "- поле"))
        self.createBtn.setText(_translate("MainWindow", "Создать"))
        self.cansBtn.setText(_translate("MainWindow", "Отмена"))
