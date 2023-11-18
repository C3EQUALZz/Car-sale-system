import sqlite3
import os
from .exceptions import UnCorrectPath
from typing import Optional


class Database:
    """
    Контекстный менеджер, который добавит возможность нам безопасно выполнять код, сохраняя все.
    """
    _instance = None

    def __new__(cls, database_name: Optional[str] = None):
        database_name = cls.check_path(path_to_file=database_name)
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connection = sqlite3.connect(database_name)
        return cls._instance

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if not self.is_connected():
            if exc_type is not None:
                self.connection.rollback()
            else:
                self.connection.commit()
            self.connection.close()

    def execute(self, query, params=()) -> sqlite3.Cursor | str:
        if not self.is_connected():
            raise RuntimeError("Database connection is closed.")

        cursor = self.connection.cursor()
        try:
            cursor.execute(query, params)
        except sqlite3.Error as e:
            raise e
        return cursor

    def is_connected(self) -> bool:
        try:
            self.connection.execute("SELECT 1")
            return True
        except sqlite3.Error:
            return False

    @staticmethod
    def check_path(path_to_file: Optional[str]):
        if path_to_file is None:
            return "database.sqlite"

        if not (os.path.exists(path_to_file) and Database._is_valid_database(path_to_file)):
            raise UnCorrectPath("Неправильный путь или файл")

    @staticmethod
    def _is_valid_database(path_to_file):
        try:
            with sqlite3.connect(path_to_file) as connection:
                #
                connection.execute("SELECT 1")
            return True
        except sqlite3.Error:
            return False
