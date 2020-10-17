
class Employee: 
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay
    def fullname(self):
        return self.first + ' ' + self.last

emp_1 = Employee('Lance', 'Dang', 50000)
emp_2 = Employee('Yen', 'Vu', 70000)

print(emp_1.email)
print(emp_1.fullname())