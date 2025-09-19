class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}. New balance: {self.balance}")
        else:
            print("Deposit must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        elif amount <= 0:
            print("Invalid withdrawal amount.")
        else:
            self.balance -= amount
            print(f"Withdrew: {amount}. Remaining balance: {self.balance}")

    def check_balance(self):
        print(f"Account Balance: {self.balance}")


# Example
acc = BankAccount("Alice", 1000)
acc.deposit(500)
acc.withdraw(200)
acc.check_balance()
