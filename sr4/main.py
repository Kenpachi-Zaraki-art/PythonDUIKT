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