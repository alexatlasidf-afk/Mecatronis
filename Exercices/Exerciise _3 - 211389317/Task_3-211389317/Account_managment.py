from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QPushButton, QComboBox

from Account import Account

from About import AboutWindow


class MyWindow(QWidget):
      
      def __init__(self):
        super().__init__() 

        self.accounts = {}

        self.about_window = AboutWindow()
        
        self.setWindowTitle("Account Manager")
        self.setGeometry(500,50,600,600)
        self.setStyleSheet("background-color: lightgreen; font-size:20px;")

        self.enter_id = QLineEdit("", self)
        self.enter_id.setGeometry(20,20,250,30)
        self.enter_id.setPlaceholderText("Enter id")
        self.enter_id.setStyleSheet("border: black; border: 2px solid black;")

        self.button = QPushButton('Create Account', self)
        self.button.setGeometry(280,20,150,30)
        self.button.setStyleSheet("border : 2px solid black; background-color: white;")

        self.button.clicked.connect(self.create_account)

        self.amount_input = QLineEdit(self)
        self.amount_input.setGeometry(20, 300, 200, 30)
        self.amount_input.setPlaceholderText("Enter amount")
        self.amount_input.setStyleSheet("border: 2px solid black; ")

        self.deposit_button = QPushButton('Deposit', self)
        self.deposit_button.setGeometry(240, 300, 100, 30)
        self.deposit_button.setStyleSheet("border: 2px solid black; background-color: white;")

        self.deposit_button.clicked.connect(self.depositing)

        self.withdraw_button = QPushButton('Withdraw', self)
        self.withdraw_button.setGeometry(350, 300, 100, 30)
        self.withdraw_button.setStyleSheet("border: 2px solid black; background-color: white;")

        self.withdraw_button.clicked.connect(self.withdrawing)

        self.about_button = QPushButton("About", self)
        self.about_button.setGeometry(450,550,100,30)
        self.about_button.setStyleSheet("border : 2px solid black; background-color: white;  ")

        self.about_button.clicked.connect(self.about_window_show)

        self.combo_box = QComboBox(self)
        self.combo_box.setGeometry(20,70,250,30)

        self.combo_box.currentTextChanged.connect(self.selected_account_from_list)

        self.balance_history_label = QLabel('', self)
        self.balance_history_label.setGeometry(20,335,300,50)
        self.balance_history_label.setStyleSheet("color: red, font-weight: bold;background-color: white; ")

      def about_window_show(self):
          self.about_window.show()
          

      def create_account(self):
          self.id = self.enter_id.text()

          if self.id in self.accounts:
              self.enter_id.setText("")
              self.enter_id.setPlaceholderText("Account already exists")
          else:
              self.accounts[self.id] = Account(self.id)
              self.combo_box.addItem(self.id)

      def depositing(self):
          selected_id = self.combo_box.currentText()
          amount = float(self.amount_input.text())

          current_account = self.accounts[selected_id]
          current_account.deposit(amount)
          self.balance_history_label.setText(f"Balance: {current_account.balance} NIS.")


      def withdrawing(self):
          selected_id = self.combo_box.currentText()
          amount = float(self.amount_input.text())
          current_account = self.accounts[selected_id]

          if amount > current_account.balance :
              self.amount_input.setText("Not Enough Money")
          else:
              current_account = self.accounts[selected_id]
              current_account.withdraw(amount)
              self.balance_history_label.setText(f"Balance: {current_account.balance} NIS.")

        
      def selected_account_from_list(self, selected_id):
    
        current_account = self.accounts[selected_id]
        self.balance_history_label.setText(f"Balance: {current_account.balance} NIS.")

      
if __name__== "__main__":
    app = QApplication()
    window = MyWindow()
    window.show()
    app.exec()
    
    

    