class Employee:
    
    def __init__(self, fname, lname, pay):
        # instance variables
        self.fname = fname 
        self.lname = lname
        self.pay = pay
        self.email = fname + '.' + lname + '@mycompany.com'

    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)


#emp_1 = Employee('Corey', 'Schafer', 50000)
#Employee.fullname(emp_1) <=> print(emp_1.fullname())