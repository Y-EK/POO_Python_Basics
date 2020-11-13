from employee import Employee

class Manager(Employee):

    def __init__(self, fname, lname, pay, employees=None):
        super().__init__(fname, lname, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees


    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)  
        
    
    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


mgr = Manager('Remi', 'Reboule', 100000)
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Thibault', 'hedy', 60000)
emp_3 = Employee('test', 'tlname', 50000)
mgr.add_employee(emp_1)
mgr.add_employee(emp_2)
mgr.add_employee(emp_3)

mgr.print_emps()