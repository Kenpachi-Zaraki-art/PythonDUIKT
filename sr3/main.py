from employee import Employee
from manager import Manager


emp1 = Employee("Alice", 15000, 28, 5)
emp2 = Employee("Bob", 12000, 25, 3)

mgr1 = Manager("Charlie", 20000, 30, subordinates=5, bonus_percent=10)

employees = [emp1, emp2, mgr1]