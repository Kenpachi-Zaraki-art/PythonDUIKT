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

    def update_student(self, student_id: int, new_pib: str = None, new_group: str = None):
        """
        Метод для оновлення даних студента.
        """
        try:
            if new_pib:
                self.cursor.execute("UPDATE students SET pib = ? WHERE id = ?", (new_pib, student_id))
            if new_group:
                self.cursor.execute("UPDATE students SET group_number = ? WHERE id = ?", (new_group, student_id))
            self.conn.commit()
            print(f"Оновлено дані для student_id {student_id}")
        except sqlite3.Error as e:
            print(f"Помилка оновлення студента: {e}")

    def get_student_data_by_id(self, student_id: int) -> dict:
        """
        Додатковий метод для читання даних з БД (частина CRUD).
        """
        try:
            # Отримуємо дані студента
            self.cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
            student_row = self.cursor.fetchone()
            if not student_row:
                print(f"Студента з ID {student_id} не знайдено.")
                return None

            student_data = {
                "id": student_row[0],
                "pib": student_row[1],
                "group": student_row[2],
                "dob": student_row[3],
                "address": student_row[4],
                "grades": []
            }

            # Отримуємо оцінки студента
            self.cursor.execute("SELECT subject, real_grade, desired_grade FROM grades WHERE student_id = ?",
                                (student_id,))
            grades_rows = self.cursor.fetchall()

            for row in grades_rows:
                student_data["grades"].append({
                    "subject": row[0],
                    "real_grade": row[1],
                    "desired_grade": row[2]
                })

            return student_data
        except sqlite3.Error as e:
            print(f"Помилка отримання даних: {e}")
            return None

    def delete_student(self, student_id: int):
        """
        Метод для видалення даних з БД.
        Завдяки 'ON DELETE CASCADE' при створенні таблиці,
        оцінки видаляться автоматично разом зі студентом.
        """
        try:
            self.cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
            self.conn.commit()
            print(f"Видалено студента з ID {student_id} та всі його оцінки.")
        except sqlite3.Error as e:
            print(f"Помилка видалення студента: {e}")

    def close(self):
        """Закриває з'єднання з БД."""
        if self.conn:
            self.conn.close()
            print("З'єднання з БД закрито.")