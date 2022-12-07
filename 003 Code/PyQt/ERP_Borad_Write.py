import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from datetime import datetime
import pymysql
import re

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_Main = uic.loadUiType("C:\PyQt\ERP_Borad_Write.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WriteClass(QMainWindow, form_Main) :
    def __init__(self, userID, coopID) :
        super().__init__()
        self.setupUi(self)
        
        self.setWindowTitle("Cooperative Inventory Management Program")
        
        self.userID = userID
        self.coopID = coopID

        self.btn_borad.clicked.connect(self.btn_borad_clicked)
        self.btn_writing.clicked.connect(self.btn_writing_clicked)

    def btn_borad_clicked(self):
        from ERP_Borad import BoradClass
        self.close()
        self.Borad = BoradClass(self.userID, self.coopID)
        self.Borad.show()
        
    def btn_writing_clicked(self):
        contents = self.ContentEdit.text()
        
        con = pymysql.connect(
            host = 'inventory.c9ibzimhazfs.ap-northeast-2.rds.amazonaws.com',
            user = 'young',
            password = 'qwer1234',
            database ='erp',
            charset='utf8'
        )
        cur = con.cursor()
        
        now = datetime.now()
        self.today = now.date()
        self.Date_Created = self.today.strftime("%Y-%m-%d")
        
        cur.execute("SELECT STRAIGHT_JOIN cm.Member_name FROM coopMember cm left join coop c on cm.Coop_id = c.Coop_id  WHERE cm.Member_id = %s", (self.userID,))
        userName_cm = cur.fetchall()
        userName = re.sub("[(''),,]","", str(userName_cm))
        
        cur.execute("INSERT INTO Commu(author, post_category, text, post_date, coop_id) VALUES (%s, %s, %s, %s, %s)", (userName, "he" ,contents, self.Date_Created, self.coopID))
        
        con.commit()
        con.close()
        
        QMessageBox.about(self, "message", "Created")
        from ERP_Borad import BoradClass
        self.close()
        self.Borad = BoradClass(self.userID, self.coopID)
        self.Borad.show()
        
        
if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #WindowClass의 인스턴스 생성
    myWrite = WriteClass()

    #프로그램 화면을 보여주는 코드
    myWrite.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
    