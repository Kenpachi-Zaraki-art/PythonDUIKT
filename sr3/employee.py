# --- employee.py ---
class Employee:
    def __init__(self, name, monthly_salary, worked_days, bonus_percent=0):
        """Initialize employee attributes"""
        self._name = name
        self._monthly_salary = monthly_salary
        self._worked_days = worked_days
        self._bonus_percent = bonus_percent

    def calculate_salary(self):
        """Calculates the employee's monthly salary"""
        return (self._monthly_salary / 30) * self._worked_days

    def calculate_bonus(self):
        """Calculates the employee's bonus"""
        return (self._monthly_salary / 100) * self._bonus_percent

    # --- Getters ---
    def get_name(self):
        return self._name

    def get_salary(self):
        return self._monthly_salary

    def get_worked_days(self):
        return self._worked_days

    def get_bonus_percent(self):
        return self._bonus_percent

    # --- Setters ---
    def set_salary(self, new_salary):
        self._monthly_salary = new_salary

    def set_worked_days(self, new_days):
        self._worked_days = new_days

    def set_bonus_percent(self, new_bonus):
        self._bonus_percent = new_bonus
