#Part_1 (Task 3)

class Account:
    def __init__(self, id_num):

        self.id = id_num
        self.balance = 0
        self.history = [0]


    def deposit(self, sum):
        money_in = float(sum)
        self.balance += money_in
        self.history.append(money_in)

        print(f'Your balance is {self.balance} shekels.')

    def withdraw(self, sub):
        money_out = float(sub)
        if money_out > self.balance:
            print(" 0 shekels withdraw, not enough balance.")
        else:
            self.balance -= money_out
            self.history.append(-money_out)
            print(f'Your balance is {self.balance}')


if __name__== "__main__":
    yosi = Account(1234)
    print(yosi.balance)
    yosi.deposit(5234)
    yosi.deposit(500)
    yosi.withdraw(2000)
    yosi.withdraw(2000)
    






        