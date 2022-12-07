import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate
from PyQt5 import uic
import datetime
from dateutil.relativedelta import relativedelta
import pymysql
import re

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("C:\PyQt\ERP_Coop_View.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class CoopdataViewClass(QMainWindow, form_class) :
    def __init__(self, userID, coopID) :
        super().__init__()
        self.setupUi(self)
        
        self.setWindowTitle("Cooperative Inventory Management Program")
        
        self.userID = userID
        self.coopID = coopID
        
        self.items_coop_in = ""
            
        # 날짜 설정
        self.now = QDate.currentDate()
        self.DateEdit_coop.setDate(QDate(self.now))
        
        self.past_DateEdit.setReadOnly(True)
        
        column_headers = ['Shipment','Items','Quantity', 'Sale Price', 'Quality'] # 테이블위젯 헤더
        
        stylesheet = "::section{background-color:#ffffff}"
        self.viewtable_coop.horizontalHeader().setStyleSheet(stylesheet)
        self.viewtable_coop.verticalHeader().setStyleSheet(stylesheet)
        self.viewtable_coop.setRowCount(50)
        self.viewtable_coop.setColumnCount(5)
        self.viewtable_coop.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.viewtable_coop.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.viewtable_coop.setHorizontalHeaderLabels(column_headers)
    
        self.DateEdit_coop.dateChanged.connect(self.date_change)
        self.btn_main_coop.clicked.connect(self.btn_main_coop_clicked)
        self.btn_graph_Price.clicked.connect(self.btn_graph_Price_clicked)
        self.btn_graph_amount.clicked.connect(self.btn_graph_amount_clicked)
        self.btn_day_coop.clicked.connect(self.btn_day_coop_clicked)
        self.btn_mon_coop.clicked.connect(self.btn_monthly_coop_clicked)
        self.btn_quarter_coop.clicked.connect(self.btn_quarterly_coop_clicked)
        self.btn_year_coop.clicked.connect(self.btn_yearly_coop_clicked)
    
    def btn_main_coop_clicked(self):
        from ERP_Main import MainClass
        self.close()
        self.Main = MainClass(self.userID, self.coopID)
        self.Main.show()
        
    def btn_graph_Price_clicked(self):
        from ERP_Graph_Price import Graph_PriceClass
        self.close()
        self.Graph_Price = Graph_PriceClass(self.userID, self.coopID)
        self.Graph_Price.show()
        
    def btn_graph_amount_clicked(self):
        from ERP_Graph_Amount import Graph_AmountClass
        self.close()
        self.Graph_Amount = Graph_AmountClass(self.userID, self.coopID)
        self.Graph_Amount.show()
    
    def date_change(self):
        if self.btn_daily_clicked:
            self.viewtable_coop.clearContents()
    
    def btn_day_coop_clicked(self):
        self.viewtable_coop.clearContents()
        con = pymysql.connect(
        host = 'inventory.c9ibzimhazfs.ap-northeast-2.rds.amazonaws.com',
        user = 'young',
        password = 'qwer1234',
        database ='erp',
        charset='utf8'
        )
        cur = con.cursor()
        
        date = self.DateEdit_coop.date()
        today = date.toString("yyyy-MM-dd")

        cur.execute("SELECT * FROM warehousing_schedule WHERE Shipment_date = %s", (today,))
        
        tablerow = 0
        result = cur.fetchall()
        for row in result:
            cur.execute("SELECT Product_name FROM product WHERE Product_id = %s", (str(row[2])))     
            items_coop = cur.fetchall()
            itmes_str = re.sub("[(''),,]","", str(items_coop))
            if str(row[7]) == self.coopID:
                self.viewtable_coop.setItem(tablerow, 0, QTableWidgetItem(str(row[4])))
                self.viewtable_coop.setItem(tablerow, 1, QTableWidgetItem(itmes_str))
                self.viewtable_coop.setItem(tablerow, 2, QTableWidgetItem(str(row[3])))
                self.viewtable_coop.setItem(tablerow, 3, QTableWidgetItem(str(row[5])))
                self.viewtable_coop.setItem(tablerow, 4, QTableWidgetItem(row[6]))
                tablerow +=1
        
        self.past_DateEdit.setDate(QDate(date))
        
        con.commit()
        con.close()
        
    def btn_monthly_coop_clicked(self):
        self.viewtable_coop.clearContents()
        con = pymysql.connect(
        host = 'inventory.c9ibzimhazfs.ap-northeast-2.rds.amazonaws.com',
        user = 'young',
        password = 'qwer1234',
        database ='erp',
        charset='utf8'
        )
        cur = con.cursor()
        
        d = self.DateEdit_coop.date() 
        today = d.toString("yyyy-MM-dd")
        cur_date = datetime.datetime.strptime(today, "%Y-%m-%d")
        other_date = cur_date - relativedelta(months=1)
        month = other_date.strftime("%Y-%m-%d")
        
        cur.execute("SELECT * FROM warehousing_schedule WHERE Shipment_date BETWEEN %s AND %s ORDER BY Shipment_date", (month, today,))
        
        tablerow = 0
        result = cur.fetchall()
        for row in result:
            cur.execute("SELECT Product_name FROM product WHERE Product_id = %s", (str(row[2])))     
            items_coop = cur.fetchall()
            itmes_str = re.sub("[(''),,]","", str(items_coop))
            if str(row[7]) == self.coopID:
                self.viewtable_coop.setItem(tablerow, 0, QTableWidgetItem(str(row[4])))
                self.viewtable_coop.setItem(tablerow, 1, QTableWidgetItem(itmes_str))
                self.viewtable_coop.setItem(tablerow, 2, QTableWidgetItem(str(row[3])))
                self.viewtable_coop.setItem(tablerow, 3, QTableWidgetItem(str(row[5])))
                self.viewtable_coop.setItem(tablerow, 4, QTableWidgetItem(row[6]))
                tablerow +=1
        
        self.past_DateEdit.setDate(QDate(other_date))
           
        con.commit()
        con.close()
        
    def btn_quarterly_coop_clicked(self):
        self.viewtable_coop.clearContents()
        con = pymysql.connect(
        host = 'inventory.c9ibzimhazfs.ap-northeast-2.rds.amazonaws.com',
        user = 'young',
        password = 'qwer1234',
        database ='erp',
        charset='utf8'
        )
        cur = con.cursor()
        
        d = self.DateEdit_coop.date() 
        today = d.toString("yyyy-MM-dd")
        cur_date = datetime.datetime.strptime(today, "%Y-%m-%d")
        other_date = cur_date - relativedelta(months=3)
        quarter = other_date.strftime("%Y-%m-%d")
        
        cur.execute("SELECT * FROM warehousing_schedule WHERE Shipment_date BETWEEN %s AND %s ORDER BY Shipment_date", (quarter, today,))
        
        tablerow = 0
        result = cur.fetchall()
        for row in result:
            cur.execute("SELECT Product_name FROM product WHERE Product_id = %s", (str(row[2])))     
            items_coop = cur.fetchall()
            itmes_str = re.sub("[(''),,]","", str(items_coop))
            if str(row[7]) == self.coopID:
                self.viewtable_coop.setItem(tablerow, 0, QTableWidgetItem(str(row[4])))
                self.viewtable_coop.setItem(tablerow, 1, QTableWidgetItem(itmes_str))
                self.viewtable_coop.setItem(tablerow, 2, QTableWidgetItem(str(row[3])))
                self.viewtable_coop.setItem(tablerow, 3, QTableWidgetItem(str(row[5])))
                self.viewtable_coop.setItem(tablerow, 4, QTableWidgetItem(row[6]))
                tablerow +=1
        
        self.past_DateEdit.setDate(QDate(other_date))
           
        con.commit()
        con.close()
        
    def btn_yearly_coop_clicked(self):
        self.viewtable_coop.clearContents()
        con = pymysql.connect(
        host = 'inventory.c9ibzimhazfs.ap-northeast-2.rds.amazonaws.com',
        user = 'young',
        password = 'qwer1234',
        database ='erp',
        charset='utf8'
        )
        cur = con.cursor()
        
        d = self.DateEdit_coop.date() 
        today = d.toString("yyyy-MM-dd")
        cur_date = datetime.datetime.strptime(today, "%Y-%m-%d")
        other_date = cur_date - relativedelta(years=1)
        year = other_date.strftime("%Y-%m-%d")   
        
        cur.execute("SELECT * FROM warehousing_schedule WHERE Shipment_date BETWEEN %s AND %s ORDER BY Shipment_date", (year, today,))
        
        tablerow = 0
        result = cur.fetchall()
        for row in result:
            cur.execute("SELECT Product_name FROM product WHERE Product_id = %s", (str(row[2])))     
            items_coop = cur.fetchall()
            itmes_str = re.sub("[(''),,]","", str(items_coop))
            if str(row[7]) == self.coopID:
                self.viewtable_coop.setItem(tablerow, 0, QTableWidgetItem(str(row[4])))
                self.viewtable_coop.setItem(tablerow, 1, QTableWidgetItem(itmes_str))
                self.viewtable_coop.setItem(tablerow, 2, QTableWidgetItem(str(row[3])))
                self.viewtable_coop.setItem(tablerow, 3, QTableWidgetItem(str(row[5])))
                self.viewtable_coop.setItem(tablerow, 4, QTableWidgetItem(row[6]))
                tablerow +=1

        self.past_DateEdit.setDate(QDate(other_date))
        
        con.commit()
        con.close()
        
if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #WindowClass의 인스턴스 생성
    myCoopdataView = CoopdataViewClass()

    #프로그램 화면을 보여주는 코드
    myCoopdataView.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
    