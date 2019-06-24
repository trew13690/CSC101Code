
from Person import Person 

class Customer(Person):

    def __init__(self, name, busName, accountEmployee, accountNumber, accountSize):
        self.businessName = busName
        self.accountEmployee = accountEmployee
        self.accountSize = accountSize
        return super().__init__(name)

    def getBusinessName(self):
        return self.businessName
    
    def getAccountEmployee(self):
        return self.accountEmployee
    def getAccountSize(self):
        return self.accountSize

    