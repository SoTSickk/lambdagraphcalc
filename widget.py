from PySide6.QtWidgets import QWidget, QPushButton
from gui import Ui_Lambda

class Widget(QWidget, Ui_Lambda):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Lambda')
        self.setGeometry(200, 455, 720, 1280)
        self.setMaximumHeight(720)
        self.setMaximumWidth(1280)
        self.setMinimumHeight(720)
        self.setMinimumWidth(1280)

        self.add0.clicked.connect(self.on_button_click())
        self.add1.clicked.connect(self.on_button_click())
        self.add2.clicked.connect(self.on_button_click())
        self.add3.clicked.connect(self.on_button_click())
        self.add4.clicked.connect(self.on_button_click())
        self.add5.clicked.connect(self.on_button_click())
        self.add6.clicked.connect(self.on_button_click())
        self.add7.clicked.connect(self.on_button_click())
        self.add8.clicked.connect(self.on_button_click())
        self.add9.clicked.connect(self.on_button_click())
        self.addpoint.clicked.connect(self.on_button_click())
        self.addx.clicked.connect(self.on_button_click())
        self.addy.clicked.connect(self.on_button_click())
        self.clear.clicked.connect(self.on_button_click())
        self.decimal.clicked.connect(self.on_button_click())
        self.divide.clicked.connect(self.on_button_click())
        self.equals.clicked.connect(self.on_button_click())
        self.goback.clicked.connect(self.on_button_click())
        self.minus.clicked.connect(self.on_button_click())
        self.plus.clicked.connect(self.on_button_click())
        self.power.clicked.connect(self.on_button_click())
        self.times.clicked.connect(self.on_button_click())
    def on_button_click(self):
        button = self.sender()
        current_text = self.typedin.text()

        if button.text() == '=':
            try:
                result = str(eval(current_text))
                self.typedin.setText(result)
            except ZeroDivisionError:
                self.typedin.setText('sosi')


