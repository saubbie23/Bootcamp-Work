class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account = BankAccount(int_rate = 0.02, balance=0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        self.account.display_account_info
        return self

    def transfer_money(self, user, amount):
        self.account.withdraw(amount)
        user.account.deposit(amount)
        return self

class BankAccount:
    def __init__(self, int_rate, balance=0):
        self.balance = balance
        self.int_rate = int_rate

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance - amount > 0:
            self.balance -= amount
        else:
            print('Insufficient funds: Charging a $5 fee.')
            self.balance -= (amount + 5)
        return self

    def display_account_info(self):
        print('Balance: $' + str(self.balance))
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance *= (self.int_rate * 100)
        return self
    
acct1 = BankAccount(.3, 400)
acct2 = BankAccount(.2)

acct1.deposit(400).deposit(32).deposit(99).withdraw(44).yield_interest().display_account_info()
acct2.deposit(11).deposit(44).withdraw(88).withdraw(1).withdraw(2).withdraw(33).yield_interest().display_account_info()

user1 = User('Big Ron', 'br@69.com')
user2 = User('Scott A', 's@a.a')
user3 = User('Steaky', 'bramble@69')

user1.make_deposit(10).make_deposit(400).make_deposit(100000).make_withdrawal(44).display_user_balance()

user2.make_deposit(50).make_deposit(44).make_withdrawal(11).make_withdrawal(1).display_user_balance()

user3.make_deposit(5000).make_withdrawal(44)
user3.make_withdrawal(22).make_withdrawal(6666666).display_user_balance()

user1.transfer_money(user3, 500000).display_user_balance()
user3.display_user_balance()