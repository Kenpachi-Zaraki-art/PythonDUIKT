from employee import Employee

class Manager(Employee):
    premium_size = 1000

    def __init__(self, name, monthly_salary, worked_days, subordinates, bonus_percent=0):
        super().__init__(name, monthly_salary, worked_days, bonus_percent)
        self._subordinates = subordinates