from KALKYKATOR import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow
import sys

class Calculator(QMainWindow):#привязка к ui
    def __init__(self):
        super (Calculator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.connectButtons()#подключение кнопок

    def connectButtons(self):#инициализация кнопок
        self.ui.pushButton_13.clicked.connect(lambda:self.add_number('0')) #0
        self.ui.pushButton_2.clicked.connect(lambda:self.add_number('1')) #1
        self.ui.pushButton.clicked.connect(lambda:self.add_number('2')) #2
        self.ui.pushButton_4.clicked.connect(lambda:self.add_number('3')) #3
        self.ui.pushButton_8.clicked.connect(lambda:self.add_number('4')) #4
        self.ui.pushButton_7.clicked.connect(lambda:self.add_number('5')) #5
        self.ui.pushButton_6.clicked.connect(lambda:self.add_number('6')) #6
        self.ui.pushButton_11.clicked.connect(lambda:self.add_number('7')) #7
        self.ui.pushButton_10.clicked.connect(lambda:self.add_number('8')) #8
        self.ui.pushButton_19.clicked.connect(lambda:self.add_number('9')) #9
        self.ui.pushButton_3.clicked.connect(lambda:self.set_rusult()) #=
        self.ui.pushButton_9.clicked.connect(lambda:self.add_number('+')) #+
        self.ui.pushButton_17.clicked.connect(lambda:self.add_number('-')) #-
        self.ui.pushButton_16.clicked.connect(lambda:self.add_number('*')) #*
        self.ui.pushButton_15.clicked.connect(lambda:self.add_number('/')) #/
        self.ui.pushButton_18.clicked.connect(lambda: self.ui.textEdit.clear()) #c
        self.ui.pushButton_14.clicked.connect(lambda:self.add_number('%')) #%
        self.ui.pushButton_12.clicked.connect(lambda:self.add_number('.')) #.
    
    def add_number(self, num):
       text = self.ui.textEdit.toPlainText()
       if num == '0' and text == '':
        pass
       else:
        text += num

       self.ui.textEdit.setText(text)
    def set_rusult(self):
        text = self.ui.textEdit.toPlainText()
        result = eval(text)
        print(result)
        self.ui.textEdit.setText(str(result))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())