
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit

app = QApplication()

window = QWidget()
window.setGeometry(50,50,500,300)
#Decides the font for all the texts (text & input text)
window.setStyleSheet('font-size:20px')

#Fn+F2 : Replace name in all code
output_text = QLabel('', window) #Do not forget to asign to window!
output_text.setGeometry(20,20,300,30)
output_text.setStyleSheet('background-color:gray')

#Text for the user to enter/write
input_text = QLineEdit('', window)
input_text.setGeometry(20,80,300,30)

#פונקציה לקבל שם מהמשתמש ולהשבת תשובה
def say_hello():
    name = input_text.text() #חייב לרשום שוב טקסט כי אנחנו רוצים מזה את הטקסט,ניתן לקחת צבע..
    output_text.setText(f'Hi {name}.')

#Connecting between the fun & the input of user
#in this case, it's by presseing "Enter"
input_text.returnPressed.connect(say_hello)

window.show()
app.exec()
