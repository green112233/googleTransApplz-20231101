import googletrans
import pprint
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon

from PyQt5 import uic
form_class = uic.loadUiType("ui/mainUI.ui")[0]

trans = googletrans.Translator()

class MyWin(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self) # 제작해 놓은 ui를 불러오기
        self.setWindowTitle('한 영중일 번역기')

        self.btn1.clicked.connect(self.btn1_clicked)
        self.btn2.clicked.connect(self.init)
#pprint.pprint(googletrans.LANGUAGES)


    def btn1_clicked(self):
        result1 = trans.translate(self.lineEdit.text(), dest='en')
        result2 = trans.translate(self.lineEdit.text(), dest='ja')
        result3 = trans.translate(self.lineEdit.text(), dest='zh-cn')
        self.textEdit.append(result1.text)
        self.textEdit_2.append(result2.text)
        self.textEdit_3.append(result3.text)

    def init(self):
        self.lineEdit.clear()
        self.textEdit.clear()
        self.textEdit_2.clear()
        self.textEdit_3.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWin()
    ex.show()
    sys.exit(app.exec_())