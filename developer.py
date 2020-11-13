from employee import Employee

class Developer(Employee):
    raise_amount = 1.05

    def __init__(self, fname, lname, pay, progr_lang):
        super().__init__(fname, lname, pay)
        #Employee.__init__(self, fname, lname, pay)
        self.progr_lang = progr_lang


dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('James', 'hedy', 60000, 'Java')

print(dev_1.email)
print(dev_2.progr_lang)