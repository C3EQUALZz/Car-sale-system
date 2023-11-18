"""
Здесь у нас описывается сущность соединения с БД.
Есть поддержка методов добавления и удаления машин из БД.
"""
import os
import sqlite3
from datetime import datetime
from typing import Optional

from .database_context_manager import Database
from ..auto_inheritance import Car


class CarDatabase(Database):
    """
    Класс, который добавляет абстракции для взаимодействия с БД.
    """

    def __init__(self, path: str = None):
        self.path = path
        self.__create_tables()

    @property
    def cars(self) -> list[Car]:
        """
        Свойство, которое возвращает нам все машины из БД в виде списка
        :return: список машин
        """
        cursor = self.execute('SELECT * FROM cars')
        return cursor.fetchall()

    def __create_tables(self) -> None:
        """
        Метод, который создает таблицы и заполняет колонки.
        Выполняет скрипты, которые прописаны в queries.sql
        :return: ничего не возвращает,
        """
        #  Получаем директорию текущего скрипта
        script_dir = os.path.dirname(__file__)
        # Соединяем путь с точкой запуска, чтобы он нашел queries.sql.
        queries_path = os.path.join(script_dir, "queries.sql")

        with open(queries_path) as file:
            # Каждый SQL запрос разделен ';', поэтому мы будем так разделять и рассматривать.
            for query in file.read().split(";"):
                # Если у нас не пустая строка, то будем выполнять запрос
                if query.strip():
                    self.execute(query + ';')

    def append(self, car: Car) -> None:
        """
        Метод, который добавляет машины в нашу БД
        :param car: экземпляр класса Car
        :return: Ничего не возвращает. Добавляет в БД информацию о вашей машине.
        """
        # получаем все атрибуты у экземпляра класса
        attributes = [getattr(car, attr) for attr in car.__dict__.keys()]
        # будем добавлять безопасно через '?' во избежания SQL инъекций
        placeholders = ', '.join('?' for _ in attributes)

        self.execute(f'''
            INSERT INTO cars (
                {', '.join(car.__dict__.keys())}
            )
            VALUES ({placeholders})
        ''', attributes)

    def create_order(self, car_id: int, customer_name: str) -> Optional[str]:
        """
        Метод, который создает заказ на машину
        :param car_id: id машины
        :param customer_name: имя заказчика
        :return: добавляет в БД имя заказчика
        """
        try:
            # узнаем время с ПК
            order_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # добавляем запись в БД
            self.execute('INSERT INTO orders (car_id, customer_name, order_date) VALUES (?, ?, ?)',
                         (car_id, customer_name, order_date))
        except sqlite3.Error as e:
            return f"Error creating order: {e}"

    def remove(self, car_id: int) -> Optional[str]:
        """
        Метод, который удаляет информацию по id машины из БД
        :param car_id: id машины в БД
        :return: ничего не возвращает
        """
        try:
            self.execute('DELETE FROM cars WHERE id = ?', (car_id,))
        except sqlite3.Error as e:
            return f"Error deleting car: {e}"
