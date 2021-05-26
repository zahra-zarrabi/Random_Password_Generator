# This Python file uses the following encoding: utf-8
import random
import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtUiTools import QUiLoader


class Main(QWidget):
    def __init__(self):
        super(Main, self).__init__()
        loader = QUiLoader()
        self.ui = loader.load('dialog.ui')
        self.ui.show()

        self.ui.btn_generate.clicked.connect(self.Passgenerate)

    def Passgenerate(self):
        self.string=""
        if self.ui.rb_standard.isChecked():
            uppercase_latter=chr(random.randint(65,90))
            number=int(random.randint(0,9))
            special_character=chr(random.randint(33,47))
            rand_list=random.sample(range(8),3)
            for i in range(8):
                self.string=self.string+chr(random.randint(97,122))
            self.string=list(self.string)
            self.string[rand_list[0]]=uppercase_latter
            self.string[rand_list[1]] =str(number)
            self.string[rand_list[2]] =special_character

        elif self.ui.rb_extra.isChecked():
            uppercase_latter = random.sample(range(65, 90),2)
            number = random.sample(range(0, 9),2)
            special_character = random.sample(range(33, 47),2)
            rand_list = random.sample(range(12), 6)
            for i in range(12):
                self.string = self.string + chr(random.randint(97, 122))
            self.string = list(self.string)
            self.string[rand_list[0]] = chr(uppercase_latter[0])
            self.string[rand_list[1]] = chr(uppercase_latter[1])
            self.string[rand_list[2]] = str(number[0])
            self.string[rand_list[3]] = str(number[1])
            self.string[rand_list[4]] = chr(special_character[0])
            self.string[rand_list[5]] = chr(special_character[1])

        elif self.ui.rb_super.isChecked():
            uppercase_latter = random.sample(range(65, 90),3)
            number = random.sample(range(0, 9),3)
            special_character = random.sample(range(33, 47),2)
            rand_list = random.sample(range(20), 8)
            for i in range(20):
                self.string = self.string + chr(random.randint(97, 122))
            self.string = list(self.string)
            self.string[rand_list[0]] = chr(uppercase_latter[0])
            self.string[rand_list[1]] = chr(uppercase_latter[1])
            self.string[rand_list[2]] = chr(uppercase_latter[2])
            self.string[rand_list[3]] = str(number[0])
            self.string[rand_list[4]] = str(number[1])
            self.string[rand_list[5]] = str(number[2])
            self.string[rand_list[6]] = chr(special_character[0])
            self.string[rand_list[7]] = chr(special_character[1])

        self.string="".join(self.string)
        self.ui.lineEdit.setText(self.string)
if __name__ == "__main__":
    app = QApplication([])
    window = Main()
    # window.show()
    sys.exit(app.exec_())
