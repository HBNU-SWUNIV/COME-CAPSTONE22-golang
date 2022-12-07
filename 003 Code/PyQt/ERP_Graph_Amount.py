import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pymysql
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import re

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_Main = uic.loadUiType("C:\PyQt\ERP_Graph_Amount.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class Graph_AmountClass(QMainWindow, form_Main) :
    def __init__(self, userID, coopID) :
        super().__init__()
        self.setupUi(self)
        
        self.setWindowTitle("Cooperative Inventory Management Program")
        
        self.userID = userID
        self.coopID = coopID
        
        self.show_graph()
        
        self.btn_main.clicked.connect(self.btn_main_clicked)
    
    def btn_main_clicked(self):
        from ERP_Coop_View import CoopdataViewClass
        self.close()
        self.CoopView = CoopdataViewClass(self.userID, self.coopID)
        self.CoopView.show()
    
    
    def show_graph(self):
        con = pymysql.connect(
        host = 'inventory.c9ibzimhazfs.ap-northeast-2.rds.amazonaws.com',
        user = 'young',
        password = 'qwer1234',
        database ='erp',
        charset='utf8'
        )
        cur = con.cursor()

        cur.execute("SELECT date_format(Shipment_date, '%Y-%m-%d') FROM Shipment ORDER BY Shipment_date Limit 10")
        shipment_date = cur.fetchall()
        shipment_conv = re.sub("[(''),,]","", str(shipment_date))
        shipment_list = shipment_conv.split(' ')

        cur.execute("SELECT Shipment_amount FROM Shipment ORDER BY Shipment_amount Limit 10")
        Shipment_amount = cur.fetchall()
    
        x_values = shipment_list
        x_values_amount = Shipment_amount
        # x_month = ['Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov']
        plt.rc('font', size = 7)
        self.graph_viewer.canvas.axes.plot(x_values, x_values_amount, marker='o', color = 'red', lw = 1) # x, y, 색깔, 선너비
        self.graph_viewer.canvas.axes.legend(['red = amount'])
        self.graph_viewer.canvas.axes.set_xticks(shipment_list, fontsize = 7)
        self.graph_viewer.canvas.draw() 
        
        con.commit()
        con.close()
        
if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #WindowClass의 인스턴스 생성
    myGraph_Amount = Graph_AmountClass()

    #프로그램 화면을 보여주는 코드
    myGraph_Amount.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
    