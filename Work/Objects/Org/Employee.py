import datetime

from Person import Person


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


