class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount

        return self
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        self.balance -= amount

        return self

    def display_account_info(self):
        return self.balance

    def yield_interest(self):
        self.balance += self.balance * self.int_rate

        return self


class User:
    def __init__(self, name, email):
        self.username = name
        self.email = email
        self.account = {}
    
    def create_account(self, bank_name):
        self.account[bank_name] = BankAccount(int_rate=0.01, balance=0)
        return self
    
    def make_deposit(self, bank_name, amount):
        if not bank_name in self.account:
            print("Bank account not found.")
            return
        self.account[bank_name].deposit(amount)
        return self
    
    def make_withdrawl(self, bank_name, amount):
        self.account[bank_name].withdraw(amount)
        return self

    def display_user_balance(self):
        for key, val in self.account.items():
            print(f"{key}: {val.display_account_info()}")
        return self