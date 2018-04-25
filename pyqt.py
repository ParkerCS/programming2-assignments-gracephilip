import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()

        # Create our Layout
        grid = QGridLayout()
        self.setLayout(grid)
        self.setGeometry(100, 10, 300, 700) # top left x, top left y, width, height


        # Create our widgets

        label = QLabel("Hello World", self)
        grid.addWidget(label, 1, 1, 1, 1) # row, col, span row, span col


        label2 = QLabel("I don't know", self)
        grid.addWidget(label2, 2, 1, 1, 2)
        label2.setAlignment(Qt.AlignCenter)

        label3 = QLabel("Label 3", self)
        grid.addWidget(label3, 1, 2, 1, 1)

        btn1 = QPushButton("Push Me", self)
        grid.addWidget(btn1, 3, 1, 1, 1)

        label_btn1 = QLabel("Not Pushed", self)
        label_btn1.setText("Unpushed")
        grid.addWidget(label_btn1, 3, 2, 1, 1)

        # Slots and Signals
        # Signals are sent when an event occurs.
        # A slot is a place for the signal to go.
        btn1.clicked.connect(lambda: label_btn1.setText("Pushed"))

        lcd = QLCDNumber(self)
        lcd.display(50)
        grid.addWidget(lcd, 4, 1, 1, 2)

        sld = QSlider(Qt.Horizontal, self)
        sld.setValue(50)
        grid.addWidget(sld, 5, 1, 1, 2)

        self.combobox = QComboBox(self)
        grid.addWidget(self.combobox, 6, 1, 1, 1)
        self.combobox.addItem("Mr. Lee")
        self.combobox.addItems(["Zoe", "Grace", "Matthew"])

        checkbox = QCheckBox("Check me!", self)
        grid.addWidget(checkbox, 6, 2, 1, 1)

        lineedit = QLineEdit(self)
        grid.addWidget(lineedit, 7, 1, 1, 1)

        textedit = QTextEdit(self)
        grid.addWidget(textedit, 7, 2, 1, 1)

        calender = QCalendarWidget(self)
        grid.addWidget(calender, 8, 1, 1, 2)

        sld.valueChanged.connect(lcd.display) # true signal to slot way to do it
        self.combobox.currentTextChanged.connect(self.combo_print)



        #draw our gui
        self.show()


    def combo_print(self):
        print("My favorite is", self.combobox.currentText())



if __name__ == "__main__":
    '''main program goes here'''
    app = QApplication(sys.argv)
    gui = Window()
    sys.exit(app.exec())