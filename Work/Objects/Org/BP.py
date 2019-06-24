from Person import Person

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
    
