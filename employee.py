class Employee:

    # class attributes
    num_of_emps = 0
    raise_amount = 1.04
    
    # contructor
    def __init__(self, fname, lname, pay):
        # instance variables
        self.fname = fname 
        self.lname = lname
        self.pay = pay
        self.email = fname + '.' + lname + '@mycompany.com'
        self.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)   


emp_1 = Employee('Corey', 'Schafer', 50000)
#Employee.fullname(emp_1) <=> print(emp_1.fullname())
emp_1.apply_raise()
print(emp_1.pay)
print(emp_1.raise_amount)
print(Employee.raise_amount)
print(emp_1.__dict__)