

class Account():
    """
        Account represents a bank account

    Attributes:
        AccountName (str) ~ represents the name of the accounts
        AccountNumber (int) ~ represents the account number of the account
        Balance (int) ~ represents the total amount of money in the account

    Methods:
        deposit(amount (int)): returns (bool) ~ takes an money amount and add to the balance
        withdraw(amount (int)): returns (bool) ~ takes an money amount and substract from the balance  
        report(): returns None ~ Prints out a report of the Account object
    """
    def __init__(self, accountName, accountNumber, balance):
        self.accountName = accountName
        self.accountNumber = accountNumber
        self.balance = balance

    def getAccountName(self):
        return self.accountName
    def getAccountNumber(self):
        return self.accountNumber
    def getBalance(self):
        return self.balance


    def deposit(self,amount):
        self.balance = self.balance + amount
        return True
    def withdraw(self,amount):
        self.balance = self.balance - amount
        return True
    def report(self):
        print("-"*10)
        print("Account Name: " + self.getAccountName())
        print("Account Number: " + str(self.getAccountNumber()))
        print("Current Balence: " + str(self.getBalance()))
        print("-"*10)


TestAccount = Account("Alex's Account",123456,500000)
TestAccount.report()
TestAccount.deposit(1000)
TestAccount.withdraw(50)
TestAccount.report()