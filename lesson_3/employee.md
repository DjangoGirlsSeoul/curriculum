### Employee and Manager

Write a class `Employee` that has attributes that return the
employee's name, title, salary, and boss. (Hint: use `def __init__(self, ???)`)

Write another class, `Manager`, that extends `Employee`. `Manager`
should have an attribute that holds an array of all employees assigned
to the manager. (Hint: make an empty list for employees and make 
a class method that allows you to add employees)
Note that managers might report to higher level managers, of course.

Add a method, `bonus(multiplier)` to `Employee`. Non-manager employees
should get a bonus like this

    bonus = (employee salary) * multiplier

Managers should get a bonus based on the total salary of all of their
subordinates, as well as the manager's subordinates' subordinates, and
the subordinates' subordinates' subordinates, etc.

    bonus = (total salary of all sub-employees) * multiplier

Hint: use `isinstance(cat, Animal)` to check if your employee is a manager 
Get subordinates salaries if they are, and if not, just get their salary

#### Testing

If we have a company structured like this:

| Name    | Salary      | Title       | Boss    |
|-------- |------------ |------------ |-------- |
| Rachell | $1,000  | Founder     | nil     |
| Jin     | $78     | Manager     | Rachell |
| Hassan  | $12     | Coach       | Jin     |
| Sujin   | $10     | Coach       | Jin     |

then we should have bonuses like this:

```python
rachell = Manager(1000, "Founder", None)
jin = Manager(78, "Manager", rachell)
hassan = Employee(12, "Coach", jin)
sujin = Employee(10, "Coach", jin)


rachell.add_employee(jin)
jin.add_employee(hassan)
jin.add_employee(sujin)


rachell.bonus(5) == 500
jin.bonus(4) == 88
sujin.bonus(3) == 30
```
