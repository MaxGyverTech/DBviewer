import sys, os
from PyQt5 import QtWidgets,QtGui,QtCore
from database.database import DB

from mypyUI import Ui_main, Ui_new_table,Ui_linePlCombo

class Main(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        #init
        super(Main,self).__init__(parent)
        self.ui = Ui_main.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('DB view by MGT')
        self.setWindowIcon(QtGui.QIcon('icon.ico'))
        self.setActive()
        # vars
        self.datatypes = ['TEXT','INT','NUMERIC','REAL','NONE']
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
        self.ui.newWriteBtn.clicked.connect(self.newpole)
        self.ui.cansBtn.clicked.connect(self.close)
        self.setWindowTitle('Создать таблицу')
        self.crDict = {}
#         self.ui.textEditE.setPlainText(
#             '''name1 = 'INT',\nname2 = 'TEXT'
# ''')

        self.ui.createBtn.clicked.connect(self.createTB)

    def createTB(self):
        # name = self.ui.tableNameE.text()
        # d = self.ui.textEditE.toPlainText()
        # print(d,name)
        # tabledict = dict(eval(d))
        # print(tabledict)
        # self.parent().db.createTable(table=name,structure=tabledict)
        pass
    def updlist(self):
        self.items = []
        for i in self.crDict:
            # self.items.append(QtWidgets.QListWidgetItem())
            t = str(i) + '  ' + self.crDict[i]
            self.ui.listWidget.addItem(t)
    def newpole(self):
        self.pole = CastLineCombo(self,txt1='Название столбца',txt2='Тип данных',itemstxt=self.parent().datatypes,varname='crDict')
        self.pole.show()

class CastLineCombo(QtWidgets.QMainWindow):
    def __init__(self,parent=None,txt1='Введите',txt2='выбирете',itemstxt=[],varname=''):
        super(CastLineCombo,self).__init__(parent)
        self.ui = Ui_linePlCombo.Ui_MainWindow()
        self.ui.setupUi(self)
        self.var = varname
        # UI
        self.ui.txt1.setText(txt1)
        self.ui.txt2.setText(txt2)
        self.ui.comboBox.addItems(itemstxt)
        # bind
        self.ui.cansBtn.clicked.connect(self.close)
        self.ui.confBtn.clicked.connect(self.add)
    def add(self):
        if self.ui.edittxt.text != '':
            eval(f'self.parent().{self.var}')[self.ui.edittxt.text()] = self.ui.comboBox.currentText()
            self.parent().updlist()
            self.close()

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

