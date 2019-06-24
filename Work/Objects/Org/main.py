import datetime

class Person:

    """
    Person represent any type of person

    Attributes:
        name (str): First Name of person
       
    """

    def __init__ (self, name='Jill Mary', isEmployee=False ):
        self.name = name
        self.isEmployee = isEmployee

    def getName(self):
        return self.name

    def _isEmployee(self):
        if self.isEmployee:
            return True 
        else:
            return False    

class Employee(Person):

    """
        Employee ( Person ) - Person who works for a company 

        Attributes :
            firstName (str)
            lastName (str)
            title (str)
            department (str)
            boss (str)
            salary (int)
            start_date (datatime)

        Methods:

            
    """
    def __init__(self, firstName,title,department,boss, salary ,start_date=datetime.datetime.now() ):
        
        self.title = title
        self.department = department
        self.boss = boss
        self.salary = salary
        self.start_date = start_date
        return super().__init__(firstName)

        

    def getName(self):
        return super().getName()
    
    def getTitle(self):
        return self.title
    def getDepartment(self):
        return self.department
    def getBoss(self):
        return self.boss
    def getSalary(self):
        return self.salary
    def getStart_Date(self):
        return self.start_date
class BP(Person):

    def __init__(self, name, company, employees, businessType ):
       self.company = company
       self.employees = employees
       self.businessType = businessType
       return super().__init__(name)

    def getCompany(self):
        return self.company
    def getEmployees(self):
        return self.employees
    def getBusinessType(self):
        return self.businessType
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

    

def start():
    directory = ReadData()
    displayDirectroy(directory)

def displayDirectroy(directory):
    Employees = []
    Customers = []
    BPs = []
    for person in directory:
        personDetail =  person.split(',')
        person = [person.replace(',', '') for person in personDetail]
        if person[0] == 'Employee':
            NewEmployee = Employee(person[1] , person[2]  , person[3], person[4], person[5], person[6])
            Employees.append(NewEmployee)
        elif person[0] == 'Customer':
            NewCustomer = Customer(person[1], person[2], person[3], person[4], person[5])
            Customers.append(NewCustomer)
        elif person[0] == 'Business Partner':
            NewBP = BP(person[1], person[2], person[3], person[4])
            BPs.append(NewBP)

    print('\nEmployees:')
    print('-'*10)
    for employee in Employees:
        
        print('Employees Name:'+ employee.getName())
        print('Title: ' + employee.getTitle())
        print('Department: '+  employee.getDepartment())
        print('Boss: ' + employee.getBoss())
        print('Start Date: ' + str(employee.getStart_Date()))
        print('-'*10)

    print('\nCustomers:')
    print('-'*10)
    for customer in Customers:
        print('Customer Name:'+ customer.getName())
        print('Formal Name:' + customer.getBusinessName())
        print('Overseeing Account: '+ customer.getAccountEmployee())
        print('Account Number: ' + customer.getAccountEmployee())
        print('Account Type: ' + customer.getAccountSize())
        print('-'*10)
    print('\nBP')
    print('-'*10)
    for bp in BPs:
        print('Name: '+ bp.getName())
        print('Business: ' + bp.getCompany())
        print('Employess: '+ bp.getEmployees())
        print('Type:' + bp.getBusinessType())
        print('-' *10)


def ReadData():
    dataobject = open('Org/data.dat','r')
    dataobject = dataobject.read().split('\n')
    return dataobject

if __name__ == '__main__':
    start()