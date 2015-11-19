### Employee and Manager
직원과 매니저

Write a class `Employee` that has attributes that return the
employee's name, title, salary, and boss. (Hint: use `def __init__(self, ???)`)
직원의 이름(employee's name), 직급(title), 급여(salary)와 팀장(boss)을 return 하는 'Employee' 클래스를 만들어 보세요. (힌트: 'def __init__(self, ???)' )

Write another class, `Manager`, that extends `Employee`. `Manager`
should have an attribute that holds an array of all employees assigned
to the manager. (Hint: make an empty list for employees and make 
a class method that allows you to add employees)
Note that managers might report to higher level managers, of course.
'Employee'에서 확장되는 'Manager' 클래스도 만들어 보세요.
'Manager'는 manager에게 지정된 모든 employee를 배열하는 속성을 필히 포함하도록 하세요.
(힌트: 빈 employees list를 만들고, employees를 추가할 수 있도록 하는 class method를 만드세요.)
manager가 상위 레벨의 manager에게 보고되어야 한다고 note를 기록 해 놓으세요. 
(직급들을 manager로만 표기하고, manager 위에 또 manager, 또 manager..가 있는 구조^^)

Add a method, `bonus(multiplier)` to `Employee`. Non-manager employees
should get a bonus like this
'Employee'에 'bonus(multiplier)' method를 추가하세요.
manager가 아닌 employees는 아래와 같이 bonus를 받아야 합니다.

    bonus = (employee salary) * multiplier

Managers should get a bonus based on the total salary of all of their
subordinates, as well as the manager's subordinates' subordinates, and
the subordinates' subordinates' subordinates, etc.
manager는 그들 부하직원의 salary를 기준으로 bonus를 받아야 합니다.
부하직원이 자신들의 부하직원을 거느리고 있다면 마찬가지로 그들 부하직원의 salary를 기준으로 합니다.

    bonus = (total salary of all sub-employees) * multiplier

Hint: use `isinstance(cat, Animal)` to check if your employee is a manager 
Get subordinates salaries if they are, and if not, just get their salary
힌트: employee가 manager인지 확인하기 위해서 'isinstance(cat, Animal)'을 사용하세요.
만약 employee가 manager라면 부하직원의 salary를 가져오도록 하고, 그렇지 않다면 그냥 salary가 계산되도록 하세요.

#### Testing
테스트 해보기

If we have a company structured like this:
아래와 같은 구조를 가지는 회사에서,

| Name    | Salary      | Title       | Boss     |
|-------- |------------ |------------ |--------  |
| Rachell | $1,000      | Founder     | nil(없음)|
| Jin     | $78         | Manager     | Rachell  |
| Hassan  | $12         | Coach       | Jin      |
| Sujin   | $10         | Coach       | Jin      |

then we should have bonuses like this:
아래와 같이 bonus를 받아야 되겠지요. (회식하러 가나요?)

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
