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
