from database_manager import DatabaseManager
from student import Student
from performance import RealPerformance, DesiredPerformance
import os

# Назва файлу БД
DB_FILE = "university.db"


def demonstrate_crud():
    """
    Демонстрація всіх операцій C.R.U.D.
    (Create, Read, Update, Delete)
    """
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)
        print(f"Видалено стару БД {DB_FILE}.")

    # 1. Ініціалізація та СТВОРЕННЯ (Create) таблиць
    db = DatabaseManager(DB_FILE)
    db.create_tables_if_not_exists()


print("\n--- 1. Демонстрація ЗАПИСУ (Create) ---")

# Створюємо дані (згідно з Тема 5)
student1_data = {
    "pib": "Іванов Іван Іванович",
    "group": "ІПЗ-21",
    "dob": "2003-05-10"
}
student1_grades = [
    ("Програмування", 85, 90),
    ("Бази даних", 78, 85),
    ("Технології VoIP", 92, 95)
]

# Записуємо студента в БД
student_id = db.add_student(
    student1_data["pib"],
    student1_data["group"],
    student1_data["dob"]
)

# Записуємо оцінки
for grade in student1_grades:
    db.add_grade(student_id, grade[0], grade[1], grade[2])

print("\n--- 2. Демонстрація ЧИТАННЯ (Read) ---")

# Читаємо дані з БД
data_from_db = db.get_student_data_by_id(student_id)

if data_from_db:
    # Тепер на основі даних з БД можна створити об'єкти класів з Теми 5

    # Створюємо об'єкт Student
    student_obj = Student(
        pib=data_from_db["pib"],
        group_number=data_from_db["group"],
        dob=data_from_db["dob"]
    )
    print(f"\nСтворено об'єкт: {student_obj}")

    # Готуємо дані для Успішності
    subjects = [g["subject"] for g in data_from_db["grades"]]
    real_grades = [g["real_grade"] for g in data_from_db["grades"]]
    desired_grades = [g["desired_grade"] for g in data_from_db["grades"]]

    # Створюємо об'єкт Реальної Успішності
    real_perf = RealPerformance(subjects, real_grades)
    print(f"Предмети: {real_perf.subjects}")
    print(f"Реальні бали: {real_perf.grades}")
    print(f"Реальний середній бал: {real_perf.average_grade():.2f}")

    # Створюємо об'єкт Бажаної Успішності
    # Встановимо бажаний середній бал вручну
    desired_perf = DesiredPerformance(subjects, desired_grades, desired_avg_input=91.5)
    print(f"Бажані бали: {desired_perf.grades}")
    print(f"Бажаний середній бал (введений): {desired_perf.average_grade()}")