from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QSpinBox, QLineEdit


from About import AboutWindow


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()  #חובה!

        self.about_window = AboutWindow()

        self.setWindowTitle("My First OOP GUI")
        self.text = QLineEdit("", self)
        self.text.setGeometry(20,20,300,30)
        

        self.button = QPushButton('CLick Me', self)
        self.button.setGeometry(20,70,300,30)
        self.button.clicked.connect(self.button_method)
    

        self.about_button = QPushButton("About", self)
        self.about_button.setGeometry(20,130,100,30)

        self.about_button.clicked.connect(self.show_about)


    def button_method(self):
        self.text.setText("The button was clicked")

    def show_about(self):
        self.about_window.show()


if __name__== "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()


