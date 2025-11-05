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