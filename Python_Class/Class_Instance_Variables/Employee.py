class Employee: 

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last 
        self.email = first + '.' + last + '@example.com'
        self.pay = pay 

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Lance', 'Dang', 50000)
emp_2 = Employee('Yen', 'Vu', 70000)

print(emp_1.first)
print(emp_1.last)
print(emp_1.pay)
print(emp_1.fullname())