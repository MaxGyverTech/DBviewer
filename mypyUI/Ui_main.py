# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\MaxGyver\Documents\VS code\pyapps\firstapp\UIs\main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(695, 436)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(5, -1, -1, -1)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setMinimumSize(QtCore.QSize(100, 0))
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 695, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.openAc = QtWidgets.QAction(MainWindow)
        self.openAc.setObjectName("openAc")
        self.newTabAc = QtWidgets.QAction(MainWindow)
        self.newTabAc.setObjectName("newTabAc")
        self.delTabAc = QtWidgets.QAction(MainWindow)
        self.delTabAc.setObjectName("delTabAc")
        self.addWriteAc = QtWidgets.QAction(MainWindow)
        self.addWriteAc.setObjectName("addWriteAc")
        self.delWriteAc = QtWidgets.QAction(MainWindow)
        self.delWriteAc.setObjectName("delWriteAc")
        self.menu.addAction(self.openAc)
        self.menu_2.addAction(self.newTabAc)
        self.menu_2.addAction(self.delTabAc)
        self.menu_3.addAction(self.addWriteAc)
        self.menu_3.addAction(self.delWriteAc)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Таблица:"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.menu_2.setTitle(_translate("MainWindow", "Таблица"))
        self.menu_3.setTitle(_translate("MainWindow", "Запись"))
        self.openAc.setText(_translate("MainWindow", "Открыть"))
        self.newTabAc.setText(_translate("MainWindow", "Создать новую"))
        self.delTabAc.setText(_translate("MainWindow", "Удалить"))
        self.addWriteAc.setText(_translate("MainWindow", "Добавить"))
        self.delWriteAc.setText(_translate("MainWindow", "Удалить"))
