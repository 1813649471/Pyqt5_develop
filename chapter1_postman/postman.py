import requests

from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5 import uic


class Postman:

    def __init__(self):
        self.ui = uic.loadUi('Postman.ui')
        self.ui.pushButton.clicked.connect(self.handCalc)
        self.ui.pushButton_2.clicked.connect(self.clear)

    def handCalc(self):
        url = self.ui.lineEdit.text()
        if len(url) == 0:
            message = "请输入有效的url"  # https://fanyi.baidu.com
        else:
            # 获取请求类型
            request_type = self.ui.comboBox.currentText()
            if request_type == 'POST':
                try:
                    message = requests.post(url=url)
                    message = message.text
                except:
                    message = '这不是有效的POST请求'
            else:
                try:
                    message = requests.get(url=url)
                    message = message.text
                except:
                    message = '这不是有效的GET请求'
        self.ui.plainTextEdit.setPlainText(message)

    def clear(self):
        self.ui.plainTextEdit.setPlainText('')


app = QApplication([])
Postman = Postman()
Postman.ui.show()
app.exec_()
