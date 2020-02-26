class Employee:

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.email = f"{self.fname}.{self.lname}@testdomain.com"
        self.pay = pay

    def getName(self):
        return f"{self.fname} {self.lname}"


emp_1 = Employee("Ashutosh", "Singh", 180000)
emp_2 = Employee("Dexter", "Root", 200000)

# emp_1.fname = "Ashutosh"
# emp_1.lname = "Singh"
# emp_1.email = f"{emp_1.fname}.{emp_1.lname}@test.com"

# print(emp_1)
# print(emp_2)

# emp_2.fname = "Dexter"
# emp_2.lname = "Root"
# emp_2.email = f"{emp_2.fname}.{emp_2.lname}@test.com"

print(emp_1.email)
print(emp_2.email)

print(Employee.getName(emp_1))
# print(emp_2.getName())