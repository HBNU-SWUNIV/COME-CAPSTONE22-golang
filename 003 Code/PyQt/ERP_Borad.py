import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QBrush
from PyQt5.QtCore import Qt
from PyQt5 import uic
import pymysql
import re

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_Main = uic.loadUiType("C:\PyQt\ERP_Borad.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class BoradClass(QMainWindow, form_Main) :
    def __init__(self, userID, coopID) :
        super().__init__()
        self.setupUi(self)
        
        self.setWindowTitle("Cooperative Inventory Management Program")
    
        self.userID = userID
        self.coopID = coopID
        
        column_headers = ['Writer', 'Content','Date Created'] # 테이블위젯 헤더
        
        stylesheet = "::section{background-color:#ffffff}"
        self.boradtable.horizontalHeader().setStyleSheet(stylesheet)
        self.boradtable.verticalHeader().setStyleSheet(stylesheet)

        self.boradtable.setRowCount(50)
        self.boradtable.setColumnCount(3)
        self.boradtable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.boradtable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.boradtable.setHorizontalHeaderLabels(column_headers)
        
        table_add(self)
        
        self.btn_main.clicked.connect(self.btn_main_clicked)
        self.btn_writing.clicked.connect(self.btn_writing_clicked)
        self.boradtable.cellClicked.connect(self.boradtable_cell_clicked)

    
    def btn_main_clicked(self):
        from ERP_Main import MainClass
        self.close()
        self.Main = MainClass(self.userID, self.coopID)
        self.Main.show()
    
    def btn_writing_clicked(self):
        from ERP_Borad_Write import WriteClass
        self.close()
        self.Write = WriteClass(self.userID, self.coopID)
        self.Write.show()
    
    def boradtable_cell_clicked(self, row, column):
        if column == 1 and self.boradtable.item(row, 1):     
            con = pymysql.connect(
            host = 'inventory.c9ibzimhazfs.ap-northeast-2.rds.amazonaws.com',
            user = 'young',
            password = 'qwer1234',
            database ='erp',
            charset='utf8'
            )
            cur = con.cursor()
            
            data = self.boradtable.item(row, 1)
            
            if cur.execute("SELECT post_id FROM Commu WHERE text = %s", (data.text())):
                post_id_cm = cur.fetchall()
                post_id = re.sub("[(''),,]","", str(post_id_cm))
            else:
                pass
            
            con.commit()
            con.close()
            
            from ERP_Borad_detalis import DetalisClass
            self.close()
            self.Detalis = DetalisClass(self.userID, self.coopID, data, post_id)
            self.Detalis.show()
            
        else:
            QMessageBox.about(self, "message", "Content None")

def table_add(self):
    con = pymysql.connect(
        host = 'inventory.c9ibzimhazfs.ap-northeast-2.rds.amazonaws.com',
        user = 'young',
        password = 'qwer1234',
        database ='erp',
        charset='utf8'
    )
    cur = con.cursor()
    cur.execute("SELECT author, text, post_date FROM Commu")
    
    tablerow = 0
    result = cur.fetchall()
    for row in result:
        self.boradtable.setItem(tablerow, 0, QTableWidgetItem(row[0]))
        self.boradtable.setItem(tablerow, 1, QTableWidgetItem(row[1]))
        self.boradtable.setItem(tablerow, 2, QTableWidgetItem(str(row[2])))
        self.boradtable.item(tablerow, 1).setForeground(QBrush(Qt.blue))
        tablerow += 1
        
if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #WindowClass의 인스턴스 생성
    myBorad = BoradClass()

    #프로그램 화면을 보여주는 코드
    myBorad.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
    