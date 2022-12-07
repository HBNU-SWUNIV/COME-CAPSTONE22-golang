import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate
from PyQt5 import uic
import sqlite3 as sq
import datetime
from dateutil.relativedelta import relativedelta


#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("C:\PyQt\ERP_View.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class DataViewClass(QMainWindow, form_class) :
    def __init__(self, userID, coopID) :
        super().__init__()
        self.setupUi(self)
        
        self.setWindowTitle("Cooperative Inventory Management Program")
        
        self.userID = userID
        self.coopID = coopID
            
        # 날짜 설정
        self.now = QDate.currentDate()
        self.DateEdit.setDate(QDate(self.now))
        
        self.past_DateEdit.setReadOnly(True)
        
        column_headers = ['Shipment','Items','Quantity', 'Sale Price', 'Quality'] # 테이블위젯 헤더
        
        stylesheet = "::section{background-color:#ffffff}"
        self.viewtable.horizontalHeader().setStyleSheet(stylesheet)
        self.viewtable.verticalHeader().setStyleSheet(stylesheet)
        self.viewtable.setRowCount(50)
        self.viewtable.setColumnCount(5)
        self.viewtable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.viewtable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.viewtable.setHorizontalHeaderLabels(column_headers)
    
        self.DateEdit.dateChanged.connect(self.date_change)
        self.btn_main.clicked.connect(self.btn_main_clicked)
        self.btn_day.clicked.connect(self.btn_daily_clicked)
        self.btn_mon.clicked.connect(self.btn_monthly_clicked)
        self.btn_quarter.clicked.connect(self.btn_quarterly_clicked)
        self.btn_year.clicked.connect(self.btn_yearly_clicked)
    
    def btn_main_clicked(self):
        from ERP_Main import MainClass
        self.close()
        self.Main = MainClass(self.userID, self.coopID)
        self.Main.show()
    
    def date_change(self):
        if self.btn_daily_clicked:
            self.viewtable.clearContents()
    
    def btn_daily_clicked(self):
        self.viewtable.clearContents()
        con = sq.connect("ERP_UI.sqlite")
        cur = con.cursor()
        
        d = self.DateEdit.date()
        today = d.toString("yyyy-MM-dd")
        cur.execute("SELECT * FROM management WHERE Shipment = ? ORDER BY Shipment", (today,))
        
        tablerow = 0
        result = cur.fetchall()
        for row in result:
            if row[0] == self.userID:
                self.viewtable.setItem(tablerow, 0, QTableWidgetItem(row[1]))
                self.viewtable.setItem(tablerow, 1, QTableWidgetItem(row[2]))
                self.viewtable.setItem(tablerow, 2, QTableWidgetItem(row[3]))
                self.viewtable.setItem(tablerow, 3, QTableWidgetItem(row[4]))
                self.viewtable.setItem(tablerow, 4, QTableWidgetItem(row[5]))
                tablerow +=1
                
        self.past_DateEdit.setDate(QDate(d))
            
        con.commit()
        con.close()
        
    def btn_monthly_clicked(self):
        self.viewtable.clearContents()
        con = sq.connect("ERP_UI.sqlite")
        cur = con.cursor()
        
        d = self.DateEdit.date() 
        today = d.toString("yyyy-MM-dd")
        cur_date = datetime.datetime.strptime(today, "%Y-%m-%d")
        other_date = cur_date - relativedelta(months=1)
        month = other_date.strftime("%Y-%m-%d")
        
        cur.execute("SELECT * FROM management WHERE Shipment BETWEEN ? AND ? ORDER BY Shipment", (month, today,))
        
        tablerow = 0
        result = cur.fetchall()
        for row in result:
            if row[0] == self.userID:
                self.viewtable.setItem(tablerow, 0, QTableWidgetItem(row[1]))
                self.viewtable.setItem(tablerow, 1, QTableWidgetItem(row[2]))
                self.viewtable.setItem(tablerow, 2, QTableWidgetItem(row[3]))
                self.viewtable.setItem(tablerow, 3, QTableWidgetItem(row[4]))
                self.viewtable.setItem(tablerow, 4, QTableWidgetItem(row[5]))
                tablerow +=1

        self.past_DateEdit.setDate(QDate(other_date))
        
        con.commit()
        con.close()
        
    def btn_quarterly_clicked(self):
        self.viewtable.clearContents()
        con = sq.connect("ERP_UI.sqlite")
        cur = con.cursor()
        
        d = self.DateEdit.date() 
        today = d.toString("yyyy-MM-dd")
        cur_date = datetime.datetime.strptime(today, "%Y-%m-%d")
        other_date = cur_date - relativedelta(months=3)
        quarter = other_date.strftime("%Y-%m-%d")   
        
        cur.execute("SELECT * FROM management WHERE Shipment BETWEEN ? AND ? ORDER BY Shipment", (quarter, today,))
        
        tablerow = 0
        result = cur.fetchall()
        for row in result:
            if row[0] == self.userID:
                self.viewtable.setItem(tablerow, 0, QTableWidgetItem(row[1]))
                self.viewtable.setItem(tablerow, 1, QTableWidgetItem(row[2]))
                self.viewtable.setItem(tablerow, 2, QTableWidgetItem(row[3]))
                self.viewtable.setItem(tablerow, 3, QTableWidgetItem(row[4]))
                self.viewtable.setItem(tablerow, 4, QTableWidgetItem(row[5]))
                tablerow +=1
        
        self.past_DateEdit.setDate(QDate(other_date))
        
        con.commit()
        con.close()
        
    def btn_yearly_clicked(self):
        self.viewtable.clearContents()
        con = sq.connect("ERP_UI.sqlite")
        cur = con.cursor()
        
        d = self.DateEdit.date() 
        today = d.toString("yyyy-MM-dd")
        cur_date = datetime.datetime.strptime(today, "%Y-%m-%d")
        other_date = cur_date - relativedelta(years=1)
        year = other_date.strftime("%Y-%m-%d")   
        
        cur.execute("SELECT * FROM management WHERE Shipment BETWEEN ? AND ? ORDER BY Shipment", (year, today,))
        
        tablerow = 0
        result = cur.fetchall()
        for row in result:
            if row[0] == self.userID:
                self.viewtable.setItem(tablerow, 0, QTableWidgetItem(row[1]))
                self.viewtable.setItem(tablerow, 1, QTableWidgetItem(row[2]))
                self.viewtable.setItem(tablerow, 2, QTableWidgetItem(row[3]))
                self.viewtable.setItem(tablerow, 3, QTableWidgetItem(row[4]))
                self.viewtable.setItem(tablerow, 4, QTableWidgetItem(row[5]))
                tablerow +=1
                
        self.past_DateEdit.setDate(QDate(other_date))
        
        con.commit()
        con.close()
        
if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #WindowClass의 인스턴스 생성
    myDataView = DataViewClass()

    #프로그램 화면을 보여주는 코드
    myDataView.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
    