class Employee(object):
    def __init__(self, salary, title, boss):


class Manager(Employee):
    def __init__(self, salary, title, boss):
        self.employees = []

    def add_employee(self, employee):

    def bonus(self, multiplier):

    def total_subsalary(self):



rachell = Manager(1000, "Founder", None)
jin = Manager(78, "Manager", rachell)
hassan = Employee(12, "Coach", jin)
sujin = Employee(10, "Coach", jin)
rachell.add_employee(jin)
jin.add_employee(hassan)
jin.add_employee(sujin)


print('rachell.bonus(5) == 500: ' + str(rachell.bonus(5) == 500))

print('jin.bonus(4) == 88: ' + str(jin.bonus(4) == 88))

print('sujin.bonus(3) == 30: ' + str(sujin.bonus(3) == 30))
