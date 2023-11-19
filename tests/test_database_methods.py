"""
Здесь реализованы тесты для проверки взаимодействия с БД.
Тут создается временная БД для тестов, в которые мы добавляем элементы.
"""
import os
from unittest import TestCase, main
from backend import CarDatabase, Car


class TestCarDatabase(TestCase):

    def setUp(self):
        # Используйте временную базу данных для тестов
        self.db = CarDatabase()

    def test_append_and_remove(self):
        # Создаем тестовую машину
        test_car = Car(
            brand='Toyota',
            model='Camry',
            generation='X',
            price=25000.0,
            year=2022,
            mileage=15000,
            country='Japan',
            region='Asia'
        )

        # Добавляем машину в базу данных
        self.db.append(test_car)

        # Проверяем, что машина действительно добавлена
        cars = self.db.cars
        self.assertTupleEqual(tuple(test_car.__dict__.values()), cars[0][1:])

        # Удаляем машину из базы данных
        self.db.remove(1)  # Предполагаем, что у машины id=1

        # Проверяем, что машина удалена
        cars_after_removal = self.db.cars
        self.assertNotIn(test_car.__dict__, cars_after_removal)

    def test_create_order(self):
        # Добавляем тестовую машину
        test_car = Car(
            brand='Toyota',
            model='Camry',
            generation='X',
            price=25000.0,
            year=2022,
            mileage=15000.0,
            country='Japan',
            region='Asia'
        )
        self.db.append(test_car)

        # Создаем заказ
        order_result = self.db.create_order(car_id=1, customer_name="Test Customer")

        # Проверяем, что заказ успешно создан (без ошибок)
        self.assertIsNone(order_result)

        # Проверяем, что заказ действительно добавлен
        orders = self.db.execute('SELECT * FROM orders WHERE car_id = ?', (1,)).fetchall()
        self.assertNotEqual(len(orders), 0)

    def tearDown(self):
        # Очищаем временную базу данных после тестов
        if os.path.exists("database.sqlite"):
            os.remove("database.sqlite")


if __name__ == '__main__':
    main()
