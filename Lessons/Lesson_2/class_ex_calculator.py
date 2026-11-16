from PySide6.QtWidgets import QApplication, QWidget, QDoubleSpinBox, QPushButton, QLabel

calculator_app = QApplication()
window = QWidget()

window.setGeometry(600,200,300,400)
window.setStyleSheet('font-size:20px')


numb_1 = QDoubleSpinBox(window)
numb_1.setGeometry(75,10,150,50)
numb_1.setRange(-100,100)

addition_button = QPushButton('+', window)
addition_button.setGeometry(140,70,25,25)


numb_2 = QDoubleSpinBox(window)
numb_2.setGeometry(75,105,150,50)
numb_2.setRange(-100,100)

equal= QLabel("=",window)
equal.setGeometry(140,165,25,25)

answer = QDoubleSpinBox(window)
answer.setGeometry(75,200,150,50)
answer.setReadOnly(True)

def addition_function():
    val1=numb_1.value()
    val2=numb_2.value()
    answer.setValue(val1+val2)

addition_button.clicked.connect(addition_function)


window.show()
calculator_app.exec()