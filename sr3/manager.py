from employee import Employee

class Manager(Employee):
    premium_size = 1000

    def __init__(self, name, monthly_salary, worked_days, subordinates, bonus_percent=0):
        super().__init__(name, monthly_salary, worked_days, bonus_percent)
        self._subordinates = subordinates
    def get_subordinates(self):
        return self._subordinates

    def set_subordinates(self, count):
        self._subordinates = count

    def generate_report(self):
        return f"Manager {self._name} manages {self._subordinates} employees."

    def calculate_bonus(self):
        base_bonus = super().calculate_bonus()
        return base_bonus + (self._subordinates * Manager.premium_size)