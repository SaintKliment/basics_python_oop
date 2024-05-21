class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Insufficient balance!")
        
    def display_balance(self):
        print('Balance:', self.__balance)
    
account = BankAccount(1000)
account.display_balance()
account.deposit(500)
account.display_balance()
account.withdraw(2000)