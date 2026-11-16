from PySide6.QtWidgets import QApplication, QWidget, QSpinBox

app =QApplication()
window = QWidget()

window.setGeometry(50,50,600,300)
window.setStyleSheet('font-size:20px')

input_number = QSpinBox(window) #רק משייכים לחלון
input_number.setGeometry(30,30,200,30)
#תחילה:מגביל בין 0-99, חיובי, מה שלא נמצא המשתמש לא יכול להזין
#הגדרת טווח מספרים
input_number.setRange(-10,10)
input_number.setValue(0)  #להגדיר מספר התחלתי


output_number = QSpinBox(window)
output_number.setGeometry(30,60,200,30)
output_number.setRange(0,100)
output_number.setStyleSheet('''
    QSpinBox {
        background-color: #444444;
        color: white;
    }
    QSpinBox::up-button, QSpinBox::down-button {
        width: 0px;
        height: 0px;
        border: none;
    }
''')

output_number.setReadOnly(True)


#פונ' שמציגה ריבוע
def square_of_num():
    square = input_number.value() #לקחת את ערך המספר מהאינפוט
    output_number.setValue(square**2)

input_number.editingFinished.connect(square_of_num)




window.show()
app.exec()