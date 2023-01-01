import sys,pdb
from PyQt5.QtWidgets import *

class App(QWidget):
    def __init__(self,token_dict):
        super().__init__()
        self.title="Lexical Analizer"
        self.left=400
        self.top=300
        self.width=800
        self.height=500

        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)

        self.create_table(token_dict)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)

        self.show()

    def create_table(self,token_dict):
        self.tableWidget = QTableWidget()

        self.tableWidget.setRowCount(len(token_dict))
        self.tableWidget.setColumnCount(1)
            
        self.tableWidget.setHorizontalHeaderItem(0,QTableWidgetItem('Token List'))

        for line in enumerate(token_dict.items()):
            self.tableWidget.setVerticalHeaderItem(line[0],QTableWidgetItem(line[1][0]))

        for line in enumerate(token_dict.items()):
            self.tableWidget.setItem(line[0],0, QTableWidgetItem(str(line[1][1])))

        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())
