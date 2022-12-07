import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate
from PyQt5 import uic
import sqlite3 as sq
import pymysql
import datetime
import socket
import re

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("C:\PyQt\ERP_UI.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class InventoryClass(QMainWindow, form_class) :
    def __init__(self, userID, coopID) :
        super().__init__()
        self.setupUi(self)
        
        self.setWindowTitle("Cooperative Inventory Management Program")
        
        CreateTable()
        CreateTable_call_value()
        ipCheck = internetCheck()
        
        if ipCheck == socket.gethostbyname(socket.gethostname()): 
            Coop_update()
            AddItem_update(self)
            DataDelete()
        else :
            AddItem(self)
        
        self.row = 0
        self.Shipment = 1
        self.Items = 1
        self.Quantity = 0
        self.Quality = 1
        self.Price = 0
        
        self.userID = userID
        self.coopID = coopID
      
        # 날짜 설정
        self.now = QDate.currentDate()
        self.ShipmentEdit.setDate(QDate(self.now))
        
        now = datetime.datetime.now()
        self.date_coop = now.date()
        
        qualitylist = ['A', 'B', 'C'] # 항목 리스트
        
        self.qualityBox.addItems(qualitylist) # 항목 추가
        
        column_headers = ['Shipment','Items','Quantity', 'Sale Price', 'Quality'] # 테이블위젯 헤더

        stylesheet = "::section{background-color:#ffffff}"
        self.datatable.horizontalHeader().setStyleSheet(stylesheet)
        self.datatable.verticalHeader().setStyleSheet(stylesheet)
        self.datatable.setRowCount(5)
        self.datatable.setColumnCount(5)
        self.datatable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.datatable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.datatable.setHorizontalHeaderLabels(column_headers)
        
        # 초기화
        d = self.ShipmentEdit.date()
        self.datatable.setItem(self.row, 0, QTableWidgetItem(str(d.toString("yyyy-MM-dd"))))
        
        list_text = self.ItemBox.currentText()
        self.datatable.setItem(self.row, 1, QTableWidgetItem(str(list_text)))
        
        list_qulity = self.qualityBox.currentText()
        self.datatable.setItem(self.row, 4, QTableWidgetItem(str(list_qulity)))
        
        self.ShipmentEdit.dateChanged.connect(self.date_change)
        self.ItemBox.currentIndexChanged.connect(self.Item_change)
        self.btn_main.clicked.connect(self.btn_main_clicked)
        self.quantityEdit.textChanged.connect(self.quantity_change)
        self.qualityBox.currentIndexChanged.connect(self.quality_change)
        self.priceEdit.textChanged.connect(self.price_change)
        self.addbtn.clicked.connect(self.btn_add_clicked)
        self.deletebtn.clicked.connect(self.btn_delete_clicked)
        self.savebtn.clicked.connect(self.btn_save_clicked)
    
    def btn_main_clicked(self):
        from ERP_Main import MainClass
        self.close()
        self.Main = MainClass(self.userID, self.coopID)
        self.Main.show()

    def date_change(self):
        self.Shipment = 1
        d = self.ShipmentEdit.date()
        self.datatable.setItem(self.row, 0, QTableWidgetItem(str(d.toString("yyyy-MM-dd"))))
    
    def Item_change(self):
        self.Items = 1
        list_text = self.ItemBox.currentText()
        self.datatable.setItem(self.row, 1, QTableWidgetItem(str(list_text)))
        
    def quantity_change(self):
        self.Quantity = 1
        quantity_text = self.quantityEdit.text()
        self.datatable.setItem(self.row, 2, QTableWidgetItem(str(quantity_text)))
        
    def price_change(self):
        self.Price = 1
        price_text = self.priceEdit.text()
        self.datatable.setItem(self.row, 3, QTableWidgetItem(str(price_text)))

    def quality_change(self):
        self.Quality = 1
        list_qulity = self.qualityBox.currentText()
        self.datatable.setItem(self.row, 4, QTableWidgetItem(str(list_qulity)))
    
    def btn_add_clicked(self):
        if self.Shipment == 1 and self.Items ==1 and self.Quantity == 1 and self.Price == 1 and self.Quality == 1 :
            self.row += 1
            self.Quantity = 0
            self.Price = 0

            d = self.ShipmentEdit.date()
            self.datatable.setItem(self.row, 0, QTableWidgetItem(str(d.toString("yyyy-MM-dd"))))
            
            list_text = self.ItemBox.currentText()
            self.datatable.setItem(self.row, 1, QTableWidgetItem(str(list_text)))
            
            list_qulity = self.qualityBox.currentText()
            self.datatable.setItem(self.row, 4, QTableWidgetItem(str(list_qulity)))
            
            QMessageBox.about(self, "message", "Added")
            
    def btn_delete_clicked(self):
        self.datatable.clearContents()
        self.row = 0
        QMessageBox.about(self, "message", "Deleted")
        
        d = self.ShipmentEdit.date()
        self.datatable.setItem(self.row, 0, QTableWidgetItem(str(d.toString("yyyy-MM-dd"))))
        
        list_text = self.ItemBox.currentText()
        self.datatable.setItem(self.row, 1, QTableWidgetItem(str(list_text)))
        
        list_qulity = self.qualityBox.currentText()
        self.datatable.setItem(self.row, 4, QTableWidgetItem(str(list_qulity)))
        
    def btn_save_clicked(self):
        ipCheck = internetCheck()
        if ipCheck == socket.gethostbyname(socket.gethostname()): #인터넷 연결이 되있는 경우
            try:
                CoopInsert(self)
                InsertData(self)
                QMessageBox.about(self, "message", "Saved")
            except:
                QMessageBox.about(self, "message", "Input is not valid")
        else: #인터넷 연결이 안되어있는 경우
            try:
                InsertData(self)
                InsertData_call_value(self)
                QMessageBox.about(self, "message", "Saved")
            except:
                QMessageBox.about(self, "message", "Input is not valid")
        

#인터넷 연결확인
def internetCheck():
    ipAddress = socket.gethostbyname(socket.gethostname())
    
    return ipAddress

#항목추가
def AddItem_update(self):
    con = pymysql.connect(
        host = 'inventory.c9ibzimhazfs.ap-northeast-2.rds.amazonaws.com',
        user = 'young',
        password = 'qwer1234',
        database ='erp',
        charset='utf8'
    )
    cur = con.cursor()
    cur.execute("SELECT Product_name FROM product")
    
    sqlite_con = sq.connect("ERP_UI_Item.sqlite")
    sqlite_cur = sqlite_con.cursor()
    
    animal_list = cur.fetchall() # 항목 리스트
    result_co = re.sub("[(',')]","", str(animal_list))
    result_conv = re.sub(r"[\[\]]","", str(result_co))
    result_list = result_conv.split(' ')
    
    for i in animal_list:
        self.ItemBox.addItem(str(i[0]))
        
    for i in range(0, len(result_list)):
        sqlite_cur.execute("INSERT INTO Items(Itme_Add) VALUES(?)", (result_list[i],))
    
    sqlite_con.commit()
    sqlite_con.close()
    
    con.commit()
    con.close()
        
def AddItem(self):
    
    sqlite_con = sq.connect("ERP_UI_Item.sqlite")
    sqlite_cur = sqlite_con.cursor()
    
    try:
        #새로 테이블을 만들어야 하는 경우
        sqlite_cur.execute("CREATE TABLE Items(Itme_Add TEXT)")
    except:
        #있으면 패스
        pass
    
    sqlite_cur.execute("SELECT DISTINCT Itme_Add FROM Items")
    
    result = sqlite_cur.fetchall()
    result_co = re.sub("[(',')]","", str(result))
    result_conv = re.sub(r"[\[\]]","", str(result_co))
    result_list = result_conv.split(' ')
    
    for i in range(0, len(result_list)):
        self.ItemBox.addItem(result_list[i])
    
    sqlite_con.commit()
    sqlite_con.close()
    

# 협동조합 DB 추가
def DataDelete():
    sqlite_con = sq.connect("ERP_UI_call.sqlite")
    sqlite_cur = sqlite_con.cursor()
    
    sqlite_cur.execute("DELETE FROM management_call")

    sqlite_con.commit()
    sqlite_con.close()

def Coop_update():
    con = pymysql.connect(
        host = 'inventory.c9ibzimhazfs.ap-northeast-2.rds.amazonaws.com',
        user = 'young',
        password = 'qwer1234',
        database ='erp',
        charset='utf8'
    )
    cur = con.cursor()
    
    sqlite_con = sq.connect("ERP_UI_call.sqlite")
    sqlite_cur = sqlite_con.cursor()
    
    sqlite_cur.execute("SELECT * FROM management_call")
    
    result = sqlite_cur.fetchall()
    result_co = re.sub("[(',')]","", str(result))
    result_conv = re.sub(r"[\[\]]","", str(result_co))
    result_list= result_conv.split(' ')

    if not result_list:
        for i in range(0, len(result_list), 8):
            if cur.execute("SELECT Product_id FROM product WHERE Product_name = %s", result_list[i + 2]):
                item_in = cur.fetchall()

            cur.execute("INSERT INTO warehousing_schedule (Member_id, Shipment_date, product_id, Shipment_amount, Req_price, Product_quailty, Coop_id, Member_update_date) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)",
                        (result_list[i], result_list[i + 1], item_in, result_list[i + 3], result_list[i + 4], result_list[i + 5], result_list[i + 6], result_list[i + 7]))
    
    else:
        pass
    
    sqlite_con.commit()
    sqlite_con.close()
    
    con.commit()
    con.close()

def CoopInsert(self):
    con = pymysql.connect(
        host = 'inventory.c9ibzimhazfs.ap-northeast-2.rds.amazonaws.com',
        user = 'young',
        password = 'qwer1234',
        database ='erp',
        charset='utf8'
    )
    cur = con.cursor()
    
    count = 0
    row = self.datatable.rowCount()
    for i in range(0, row):
        if self.datatable.item(i, count):
            Shipment_coop = self.datatable.item(i, 0)
            Items_coop = self.datatable.item(i, 1)
            Quantity_coop = self.datatable.item(i, 2)
            Sale_Price_coop = self.datatable.item(i, 3)
            Quality_coop = self.datatable.item(i, 4)
            count += 1
    
            if cur.execute("SELECT Product_id FROM product WHERE Product_name = %s", (Items_coop.text(),)):
                items_coop_in = cur.fetchall()
            
            cur.execute("INSERT INTO warehousing_schedule (Member_id, Shipment_date, product_id, Shipment_amount, Req_price, Product_quailty, Coop_id, Member_update_date) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)",
                        (self.userID, Shipment_coop.text(), items_coop_in, Quantity_coop.text(), Sale_Price_coop.text(),Quality_coop.text(), self.coopID, self.date_coop))
    
    cur.fetchall()
    con.commit()
    con.close()

#SQLite
def CreateTable():
    con = sq.connect("ERP_UI.sqlite")
    cur = con.cursor()
    
    try:
        #새로 테이블을 만들어야 하는 경우
        cur.execute("CREATE TABLE management(Member_id TEXT, Shipment TEXT, Items TEXT, Quantity TEXT, SalePrice TEXT, Quality TEXT, Coop_id TEXT, Member_update_date TEXT)")
    except:
        #있으면 패스
        pass
    
    cur.fetchall()
    
    con.commit()
    con.close()
    
def InsertData(self):
    
    con = sq.connect("ERP_UI.sqlite")
    cur = con.cursor()
    
    count = 0
    row = self.datatable.rowCount()
    for i in range(0, row):
        if self.datatable.item(i, count):
            Shipment_data = self.datatable.item(i, 0)
            Items_data = self.datatable.item(i, 1)
            Quantity_data = self.datatable.item(i, 2)
            Sale_Price_data = self.datatable.item(i, 3)
            Quality_data = self.datatable.item(i, 4)
            count += 1
    
            cur.execute("INSERT INTO management VALUES(?, ?, ?, ?, ?, ?, ?, ?)",
                        (self.userID, Shipment_data.text(), Items_data.text(), Quantity_data.text(), Sale_Price_data.text(),Quality_data.text(), self.coopID, self.date_coop))
    
    cur.fetchall()
    con.commit()
    con.close()
    
def CreateTable_call_value():
    con = sq.connect("ERP_UI_call.sqlite")
    cur = con.cursor()
    
    try:
        #새로 테이블을 만들어야 하는 경우
        cur.execute("CREATE TABLE management_call(Member_id TEXT, Shipment TEXT, Items TEXT, Quantity TEXT, SalePrice TEXT, Quality TEXT, Coop_id TEXT, Member_update_date TEXT)")
    except:
        #있으면 패스
        pass
    
    cur.fetchall()
    
    con.commit()
    con.close()
    
def InsertData_call_value(self):
    
    con = sq.connect("ERP_UI_call.sqlite")
    cur = con.cursor()
    
    count = 0
    row = self.datatable.rowCount()
    for i in range(0, row):
        if self.datatable.item(i, count):
            Shipment_data = self.datatable.item(i, 0)
            Items_data = self.datatable.item(i, 1)
            Quantity_data = self.datatable.item(i, 2)
            Sale_Price_data = self.datatable.item(i, 3)
            Quality_data = self.datatable.item(i, 4)
            count += 1
    
            cur.execute("INSERT INTO management_call VALUES(?, ?, ?, ?, ?, ?, ?, ?)",
                        (self.userID, Shipment_data.text(), Items_data.text(), Quantity_data.text(), Sale_Price_data.text(),Quality_data.text(), self.coopID, self.date_coop))
    
    cur.fetchall()
    con.commit()
    con.close()

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #WindowClass의 인스턴스 생성
    myInventory = InventoryClass()

    #프로그램 화면을 보여주는 코드
    myInventory.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
    