from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QSpinBox, QLineEdit, QLabel

from PySide6.QtGui import QPixmap

from PySide6.QtCore import Qt  

from PySide6.QtCore import QUrl

from PySide6.QtGui import QDesktopServices

class AboutWindow(QWidget):

    def __init__(self):
        super().__init__() 

        self.setWindowTitle("About Window")
        self.setGeometry(500,100,380,500)
        self.setStyleSheet("background-color: white; ")

        self.name = QLabel("ALEX ATLAS\n26\nAlex.Atlas@s.afeka.ac.il", self)
        self.name.setGeometry(20,20,300,100)
        self.name.setStyleSheet("background-color: green; border: 3px solid black; color: black;font-size: 15px; font-weight: bold ")
        self.name.setAlignment(Qt.AlignCenter)
        
        self.my_pic = QLabel(self)
        self.my_pic.setGeometry(20,120,300,300)


        image = QPixmap("SHREK.webp").scaled(300,300)
        self.my_pic.setPixmap(image)

        self.link_button = QPushButton('My Link',self)
        self.link_button.setGeometry(100,450,150,30)
        self.link_button.setStyleSheet("background-color: red; color: white; border: 3px solid white; font-size: 13px; font-weight: bold")

        self.link_button.clicked.connect(self.open_link)

    def open_link(self):
        QDesktopServices.openUrl(QUrl("https://www.linkedin.com/in/alex-atlas-09292344b/"))


if __name__== "__main__":
    app = QApplication()
    window = AboutWindow()
    window.show()
    app.exec()
