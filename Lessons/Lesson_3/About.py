from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QSpinBox, QLineEdit, QLabel

from PySide6.QtGui import QPixmap

from PySide6.QtCore import Qt          # only needed for scaling options


class AboutWindow(QWidget):

    def __init__(self):
        super().__init__() 

        self.setWindowTitle("About Window")

        self.name = QLabel("ALEX", self)
        self.name.setGeometry(20,20,300,30)

        self.my_pic = QLabel(self)
        self.my_pic.setGeometry(20,60,300,300)


        image = QPixmap("SHREK.webp").scaled(300,300)
        self.my_pic.setPixmap(image)

    



if __name__== "__main__":
    app = QApplication()
    window = AboutWindow()
    window.show()
    app.exec()
