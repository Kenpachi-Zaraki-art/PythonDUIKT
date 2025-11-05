class Student:
    def __init__(self, pib: str, group_number: str, dob: str = None, address: str = None):
        self.__pib = pib
        self.__group_number = group_number
        self.__dob = dob  # Дата народження
        self.__address = address  # Адреса