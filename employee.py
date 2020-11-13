import datetime
from datetime import date

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
        
        Employee.num_of_emps += 1

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.fname, self.lname, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    # Object Methods
    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)   

    # Class methods
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        fname, lname, pay = emp_str.split('-')
        return cls(fname, lname, pay)

    # Static methods
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True