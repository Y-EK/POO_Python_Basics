from employee import Employee

class Developer(Employee):
    raise_amount = 1.05

    def __init__(self, fname, lname, pay, progr_lang):
        super().__init__(fname, lname, pay)
        #Employee.__init__(self, fname, lname, pay)
        self.progr_lang = progr_lang