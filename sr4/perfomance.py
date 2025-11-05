from abc import ABC, abstractmethod
from typing import List, Union

class Performance(ABC):
    """
    Абстрактний клас УСПІШНІСТЬ.
    Визначає базову структуру для списку предметів та балів.
    """
    def __init__(self, subjects: List[str], grades: List[int]):
        self.subjects = subjects
        self.grades = grades

    @abstractmethod
    def average_grade(self) -> float:
        """
        Абстрактний метод для обчислення середнього балу.
        """
        pass
class RealPerformance(Performance):
    """
    Клас для реальної успішності.
    Реалізує метод average_grade для обчислення реального середнього балу.
    """
    def average_grade(self) -> float:
        """
        Обчислює реальний середній бал.
        """
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)


class DesiredPerformance(Performance):
    """
    Клас БАЖАНА_УСПІШНІСТЬ, наслідує Performance.
    Список балів тут - це "Список бажаних балів".
    """

    def __init__(self, subjects: List[str], grades: List[int], desired_avg_input: float = None):
        super().__init__(subjects, grades)
        # Додаткове поле для "введеного студентом" середнього балу
        self.__desired_average_input = desired_avg_input

    def average_grade(self) -> float:
        """
        Повертає бажаний середній бал, введений студентом.
        Якщо він не введений, для демонстрації обчислимо середній з бажаних балів.
        """
        if self.__desired_average_input is not None:
            return self.__desired_average_input  #

        # Альтернативна логіка, якщо бал не введено
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    @property
    def desired_average(self) -> float:
        return self.average_grade()

    @desired_average.setter
    def desired_average(self, value: float):
        self.__desired_average_input = value