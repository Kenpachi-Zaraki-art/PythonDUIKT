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