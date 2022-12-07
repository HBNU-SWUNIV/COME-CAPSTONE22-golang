import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from ERP_Main import MainClass
import sqlite3 as sq
import pymysql
import re
import socket

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_login = uic.loadUiType("C:\PyQt\ERP_Login.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class LoginClass(QMainWindow, form_login) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        self.setWindowTitle("Cooperative Inventory Management Program")
        
        sqlite_con = sq.connect("ERP_Login.sqlite")
        sqlite_cur = sqlite_con.cursor()
        
        try:
        #새로 테이블을 만들어야 하는 경우
            sqlite_cur.execute("CREATE TABLE Login(Member_id INTEGER PRIMARY KEY, Member_name TEXT, Member_pw TEXT, Coop_name TEXT, Coop_id TEXT)")
        except:
            #있으면 패스
            pass
        
        ipCheck = internetCheck()
        if ipCheck == socket.gethostbyname(socket.gethostname()): #인터넷 연결이 되있는 경우
            con = pymysql.connect(
                host = 'inventory.c9ibzimhazfs.ap-northeast-2.rds.amazonaws.com',
                user = 'young',
                password = 'qwer1234',
                database ='erp',
                charset='utf8'
            )
            cur = con.cursor()
            
            cur.execute("SELECT STRAIGHT_JOIN cm.Member_name, cm.Member_pw, c.Coop_name, c.Coop_id FROM coopMember cm left join coop c on cm.Coop_id = c.Coop_id")
            login = cur.fetchall()
            login_conv = re.sub("[('')]","", str(login))
            login_list_conv = login_conv.split(',')
            login_list = []
            
            for i in login_list_conv:
                i = i.strip()
                login_list.append(i)
            
            # count = 94
            # for i in range(0, len(login_list), 4):
            #     sqlite_cur.execute("INSERT INTO Login(Member_id, Member_name, Member_pw, Coop_name, Coop_id) VALUES(?, ?, ?, ?, ?)", (count, login_list[i], login_list[i + 1], login_list[i + 2], login_list[i + 3],))
            #     count += 1
                
            sqlite_con.commit()
            sqlite_con.close()
            
            con.commit()
            con.close()
        
        self.btnlogin.clicked.connect(self.btn_login_clicked)

    def btn_login_clicked(self):
        userName = self.IdEdit.text()
        userPwd = self.nameEdit.text()
        coopName = self.coopIdEdit.text()
        
        sqlite_con = sq.connect("ERP_Login.sqlite")
        sqlite_cur = sqlite_con.cursor()
     
        sqlite_cur.execute("SELECT Member_name, Member_pw, Coop_name FROM Login WHERE Member_name = ? AND Member_pw = ? AND Coop_name = ? ", (userName, userPwd, coopName,))
        
        if sqlite_cur.fetchall():
                
            sqlite_cur.execute("SELECT Member_id FROM Login WHERE Member_name = ?", (userName,))
            userID_cm = sqlite_cur.fetchall()
            userID_conv = re.sub("[(''),,]","", str(userID_cm))
            userID = re.sub(r"[\[\]]","", str(userID_conv))
            
            sqlite_cur.execute("SELECT Coop_id FROM Login WHERE Member_name = ?", (userName,))
            coopID_cm = sqlite_cur.fetchall()
            coopID_conv = re.sub("[(''),,]","", str(coopID_cm))
            coopID = re.sub(r"[\[\]]","", str(coopID_conv))
            
            self.close()
            self.Main = MainClass(userID, coopID)
            self.Main.show()
        
            sqlite_con.commit()
            sqlite_con.close()
        
        else:
            QMessageBox.about(self, "message", "Login failed")
            
def internetCheck():
    ipAddress = socket.gethostbyname(socket.gethostname())
    
    return ipAddress
        
if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #WindowClass의 인스턴스 생성
    myLogin = LoginClass()
    
    #프로그램 화면을 보여주는 코드
    myLogin.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
    