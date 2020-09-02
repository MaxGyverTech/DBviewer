import sys, os
from PyQt5 import QtWidgets,QtGui,QtCore
from database.database import DB

from mypyUI import Ui_main, Ui_new_table

class Main(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        #init
        super(Main,self).__init__(parent)
        self.ui = Ui_main.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('DB view by MGT')
        self.setWindowIcon(QtGui.QIcon('icon.ico'))
        self.setActive()
        #trigers
        self.ui.openAc.triggered.connect(self.browsefile)
        self.ui.newTabAc.triggered.connect(self.create_table)
        self.ui.comboBox.currentTextChanged.connect(self.tableselected)
    
    def setActive(self,val:bool = False):
        s = self.ui
        s.addWriteAc.setEnabled(val)
        s.newTabAc.setEnabled(val)
        s.delTabAc.setEnabled(val)
        s.delWriteAc.setEnabled(val)

    def browsefile(self):
        file = QtWidgets.QFileDialog.getOpenFileName(self, 'Выберите файл БД',filter='*.db *.sqlite')[0]
        db = DB(file,debug=True)
        print(file)
        self.db = db
        tables = db.gettables()
        print(tables)
        self.setActive(True)
        for i in tables:
            self.ui.comboBox.addItem(i[0])
    
    def tableselected(self,value):
        self.ui.statusbar.showMessage('Можете редактировать ячейки они сразу сохранятся',msecs=10000)
        self.db.setdefaulttable(value)
        columns = self.db.getcolumns()
        print(columns)
        self.ui.tableWidget.setColumnCount(len(columns))
        self.ui.tableWidget.setHorizontalHeaderLabels(columns)
        data = self.db.getall()
        self.ui.tableWidget.setRowCount(len(data))
        row = 0
        for tup in data:
            col = 0
            for item in tup:
                val = QtWidgets.QTableWidgetItem(str(item))
                print(row,col,item)
                self.ui.tableWidget.setItem(row, col, val)
                col += 1
 
            row += 1
        self.ui.tableWidget.resizeColumnsToContents()
        self.ui.tableWidget.itemChanged.connect(self.editcell)

    def editcell(self,item:QtWidgets.QTableWidgetItem):
        col = self.db.getcolumns()[item.column()]
        row = item.row() + 1
        val = item.text()
        print('bpvtytyj ',row,col,val)
        self.db.edit(value=val,idvalue=row,column=col,idcolumn='rowid')
        self.ui.tableWidget.resizeColumnsToContents()
    def create_table(self):
        self.createTb = CreateTableWindow(self)
        self.createTb.show()

class CreateTableWindow(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        super(CreateTableWindow,self).__init__(parent)
        self.ui = Ui_new_table.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Создать таблицу')
        self.ui.textEditE.setPlainText(
            '''name1 = 'INT',\nname2 = 'TEXT'
''')

        self.ui.createBtn.clicked.connect(self.createTB)

    def createTB(self):
        name = self.ui.tableNameE.text()
        d = self.ui.textEditE.toPlainText()
        print(d,name)
        tabledict = dict(eval(d))
        print(tabledict)
        self.parent().db.createTable(table=name,structure=tabledict)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

