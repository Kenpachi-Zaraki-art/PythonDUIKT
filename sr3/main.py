from employee import Employee
from manager import Manager


emp1 = Employee("Alice", 15000, 28, 5)
emp2 = Employee("Bob", 12000, 25, 3)

mgr1 = Manager("Charlie", 20000, 30, subordinates=5, bonus_percent=10)

employees = [emp1, emp2, mgr1]

for emp in employees:
    print(f"Employee: {emp.get_name()}")
    print(f"  Salary: {emp.calculate_salary()} UAH")
    print(f"  Bonus: {emp.calculate_bonus()} UAH")
    if isinstance(emp, Manager):
        print(f"  Report: {emp.generate_report()}")
    print("-" * 40)

input("Press Enter to exit...")