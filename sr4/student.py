class Student:
    def __init__(self, pib: str, group_number: str, dob: str = None, address: str = None):
        self.__pib = pib
        self.__group_number = group_number
        self.__dob = dob  # Дата народження
        self.__address = address  # Адреса

        # --- Гетер для ПІБ ---
        @property
        def pib(self) -> str:
            return self.__pib

        # --- Сетер для ПІБ ---
        @pib.setter
        def pib(self, new_pib: str):
            if isinstance(new_pib, str) and len(new_pib) > 5:  # Проста валідація
                self.__pib = new_pib
            else:
                print("Помилка: ПІБ має бути рядком довжиною більше 5 символів.")

        # --- Гетер для Номера групи ---
        @property
        def group_number(self) -> str:
            return self.__group_number

        # --- Сетер для Номера групи ---
        @group_number.setter
        def group_number(self, new_group: str):
            self.__group_number = new_group

        # --- Гетери та сетери для додаткових полів ---
        @property
        def dob(self) -> str:
            return self.__dob

        @dob.setter
        def dob(self, new_dob: str):
            self.__dob = new_dob

        @property
        def address(self) -> str:
            return self.__address

        @address.setter
        def address(self, new_address: str):
            self.__address = new_address

        def __str__(self):
            return f"Студент: {self.pib}, Група: {self.group_number}"