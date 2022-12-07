import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread, pyqtSlot
from PyQt5 import QtCore 
from PyQt5 import uic

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_Main = uic.loadUiType("C:\PyQt\ERP_Chat.ui")[0]

class SocketClient(QThread):
    add_chat = QtCore.pyqtSignal(str)
    
    def __init__(self, parent = None):
        super().__init__()
        self.main = parent
        self.is_run = False
    
    def run(self):
        self.is_run = not self.is_run
        self.add_chat.emit('Server Connection Complete')

#화면을 띄우는데 사용되는 Class 선언
class BoradClass(QMainWindow, form_Main) :
    def __init__(self, userID, coopID) :
        super().__init__()
        self.setupUi(self)
        
        self.setWindowTitle("Cooperative Inventory Management Program")
        
        self.userID = userID
        self.coopID = coopID
        
        self.ChatEdit.setReadOnly(True)
        
        self.connbtn.clicked.connect(self.btn_connection_clicked)
        self.sendbtn.clicked.connect(self.btn_send_clicked)
        self.btn_main.clicked.connect(self.btn_main_clicked)
        self.sc = SocketClient(self)
        self.sc.add_chat.connect(self.add_chat)
        
    def btn_main_clicked(self):
        from ERP_Main import MainClass
        self.close()
        self.Main = MainClass(self.userID, self.coopID)
        self.Main.show()
    
    def btn_connection_clicked(self):
        ip = self.IPEdit.toPlainText()
        port = self.portEdit.toPlainText()
        
        if (not ip) or (not port):
            self.add_chat('Ip or Port Number is Empty')
            return

        self.sc = SocketClient(self)
        
        if not self.sc.is_run:
            self.sc.start(1)
    
    def btn_send_clicked(self):
        if not self.sc.is_run:
            self.add_chat('Server Disconnected, Unable to Send Message')
            return
        
        msg = self.inputEdit.toPlainText()
        self.add_chat('[My] %s' %(msg))
        self.inputEdit.setPlainText('')
    
    def add_chat(self, msg):
        self.ChatEdit.appendPlainText(msg)
        
if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #WindowClass의 인스턴스 생성
    myBorad = BoradClass()

    #프로그램 화면을 보여주는 코드
    myBorad.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
    