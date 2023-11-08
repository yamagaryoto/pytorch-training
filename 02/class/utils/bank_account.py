class BankAcount:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.interest_rate = 0.01
    def deposit(self, n):
        self.balance += n
    def withdraw(self, n):
        self.balance -= n
    def get_balance(self):
        return self.balance
    def set_interest_rate(self, rate):
        self.interest_rate = rate
    def apply_interest(self):
        self.balance = self.balance * (1 + self.interest_rate)

    
