class Employee(object):
    def __init__(self, salary, title, boss):
        self.salary = salary
        self.title = title
        self.boss = boss

    def bonus(self, multiplier):
        return self.salary * multiplier

class Manager(Employee):
    def __init__(self, salary, title, boss):
        self.salary = salary
        self.title = title
        self.boss = boss
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        return self.employees

    def bonus(self, multiplier):
        return self.total_subsalary() * multiplier

    def total_subsalary(self):
        employees_salary = 0
        for employee in self.employees:
            if isinstance(employee, Manager):
                employees_salary += employee.salary + employee.total_subsalary()
            else:
                employees_salary += employee.salary
        return employees_salary

rachell = Manager(1000, "Founder", None)
jin = Manager(78, "Manager", rachell)
hassan = Employee(12, "Coach", jin)
sujin = Employee(10, "Coach", jin)
rachell.add_employee(jin)
jin.add_employee(hassan)
jin.add_employee(sujin)

print(rachell.bonus(5))
print(jin.bonus(4))
print(sujin.bonus(3))
