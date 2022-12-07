import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
import sqlite3 as sq

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_Main = uic.loadUiType("C:\PyQt\ERP_Main.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class MainClass(QMainWindow, form_Main) :
    def __init__(self, userID, coopID) :
        super().__init__()
        self.setupUi(self)
        
        self.setWindowTitle("Cooperative Inventory Management Program")
        
        self.userID = userID
        self.coopID = coopID
        
        self.btnLogout.clicked.connect(self.btn_Logout_clicked)
        self.btnitem.clicked.connect(self.btn_item_clicked)
        self.btnview.clicked.connect(self.btn_view_clicked)
        self.btncoop.clicked.connect(self.btn_coopview_clicked)
        self.btnboard.clicked.connect(self.btn_board_clicked)
    
    def btn_item_clicked(self):
        from ERP_UI import InventoryClass
        self.close()
        self.Inventory = InventoryClass(self.userID, self.coopID)
        self.Inventory.show()
        
    def btn_coopview_clicked(self):
        from ERP_Coop_View import CoopdataViewClass
        self.close()
        self.CoopView = CoopdataViewClass(self.userID, self.coopID)
        self.CoopView.show()    
    
    def btn_view_clicked(self): 
        from ERP_View import DataViewClass
        self.close()
        self.DataView = DataViewClass(self.userID, self.coopID)
        self.DataView.show()
    
    def btn_board_clicked(self):
        from ERP_Borad import BoradClass
        self.close()
        self.Borad = BoradClass(self.userID, self.coopID)
        self.Borad.show()
                
    def btn_Logout_clicked(self):
        from ERP_Login import LoginClass
        self.close()
        self.Login = LoginClass()
        self.Login.show()

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #WindowClass의 인스턴스 생성
    myMain = MainClass()

    #프로그램 화면을 보여주는 코드
    myMain.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
    