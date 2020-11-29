import sys
from PyQt5.QtWidgets import QApplication, QDialog
from demoCalculator import *


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        # Clicked event of the push button is connected with the appropriate methods
        self.ui.pushButtonPlus.clicked.connect(self.add)
        self.ui.pushButtonSubtract.clicked.connect(self.subtract)
        self.ui.pushButtonMultiply.clicked.connect(self.multiplication)
        self.ui.pushButtonDivide.clicked.connect(self.division)

        self.show()

    def extractFirstNumber(self):
        try:
            if len(self.ui.lineEditFirstNumber.text()) != 0:
                first_num = float(self.ui.lineEditFirstNumber.text())
            else:
                first_num = 0
            return first_num
        except ValueError:
            raise ValueError

    def extractSecondNumber(self):
        try:
            if len(self.ui.lineEditSecondNumber.text()) != 0:
                second_num = float(self.ui.lineEditSecondNumber.text())
            else:
                second_num = 0
            return second_num
        except ValueError:
            raise ValueError


    def add(self):
        try:
            firstnum = self.extractFirstNumber()
            secondnum = self.extractSecondNumber()
            result = firstnum + secondnum
            self.ui.labelResult.setText(f'Summation: {firstnum} + {secondnum} = {result:.4f}')
        except ValueError:
            self.ui.labelResult.setText('ValueError! Please provide a numeric value')

    def subtract(self):
        try:
            firstnum = self.extractFirstNumber()
            secondnum = self.extractSecondNumber()
            result = firstnum - secondnum
            self.ui.labelResult.setText(f'Subtraction:{firstnum} - {secondnum} = {result:.4f}')
        except ValueError:
            self.ui.labelResult.setText('ValueError! Please provide a numeric value')
    def multiplication(self):
        try:
            firstnum = self.extractFirstNumber()
            secondnum = self.extractSecondNumber()
            result = firstnum * secondnum
            self.ui.labelResult.setText(f'Multiplication: {firstnum} X {secondnum} = {result:.4f}')
        except ValueError:
            self.ui.labelResult.setText('ValueError! Please provide a numeric value')

    def division(self):
        try:
            firstnum = self.extractFirstNumber()
            secondnum = self.extractSecondNumber()
            result = firstnum / secondnum
            self.ui.labelResult.setText(f'Division: {firstnum} / {secondnum} = {result:.4f}')
        except ValueError:
            self.ui.labelResult.setText('ValueError! Please provide a numeric value')
        except ZeroDivisionError:
            self.ui.labelResult.setText(f'ZeroDivisionError! Cannot divide by zero.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    window.show()
    sys.exit(window.exec_())
