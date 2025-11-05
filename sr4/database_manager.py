import sqlite3
from typing import List, Tuple

class DatabaseManager:
    """
    Клас для управління базою даних SQLite (створення, запис, оновлення, видалення).
    """
    def __init__(self, db_file: str):
        """
        Ініціалізує з'єднання з файлом БД.
        """
        try:
            self.conn = sqlite3.connect(db_file)
            self.cursor = self.conn.cursor()
            print(f"Успішно підключено до {db_file}")
        except sqlite3.Error as e:
            print(f"Помилка підключення до БД: {e}")
            self.conn = None

    def create_tables_if_not_exists(self):
        """
        Реалізує метод роботи з таблицями (створення, якщо відсутні).
        """
        if not self.conn:
            return

        # Таблиця Студентів
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pib TEXT NOT NULL,
            group_number TEXT NOT NULL,
            dob TEXT,
            address TEXT
        );
        """)

        # Таблиця для Успішності (реальної та бажаної)
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS grades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            subject TEXT NOT NULL,
            real_grade INTEGER,
            desired_grade INTEGER,
            FOREIGN KEY (student_id) REFERENCES students (id) ON DELETE CASCADE
        );
        """)
        self.conn.commit()
        print("Таблиці 'students' та 'grades' перевірено/створено.")

    def add_student(self, pib: str, group: str, dob: str = None, address: str = None) -> int:
        """
        Метод для запису даних студента в БД.
        Повертає ID створеного студента.
        """
        try:
            self.cursor.execute("""
            INSERT INTO students (pib, group_number, dob, address)
            VALUES (?, ?, ?, ?)
            """, (pib, group, dob, address))
            self.conn.commit()
            print(f"Додано студента: {pib}")
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Помилка додавання студента: {e}")
            return -1

    def add_grade(self, student_id: int, subject: str, real_grade: int, desired_grade: int):
        """
        Метод для запису предметів та балів студента.
        """
        try:
            self.cursor.execute("""
            INSERT INTO grades (student_id, subject, real_grade, desired_grade)
            VALUES (?, ?, ?, ?)
            """, (student_id, subject, real_grade, desired_grade))
            self.conn.commit()
            print(f"Додано оцінку для student_id {student_id}: {subject}")
        except sqlite3.Error as e:
            print(f"Помилка додавання оцінки: {e}")