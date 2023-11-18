"""
TODO: Поправить тесты
"""
from unittest import TestCase, main, mock

from backend import CarDatabase, Car


class CarDatabaseTest(TestCase):
    @mock.patch('backend.CarDatabase', autospec=True)
    def test_append(self, mock_database):
        # Создаем экземпляр класса CarDatabase, используя имитацию
        car_db = CarDatabase()

        # Имитация выполнения запроса
        mock_cursor = mock_database.return_value.connection.cursor.return_value

        # Создаем объект Car для добавления
        car_to_add = Car(
            brand='Toyota',
            model='Camry',
            generation='X',
            price=25000.0,
            year=2022,
            mileage=15000.0,
            country='Japan',
            region='Asia'
        )

        # Тестирование метода append
        car_db.append(car_to_add)

        # Проверяем, что метод execute был вызван у mock_database с ожидаемыми параметрами
        mock_database.return_value.connection.execute.assert_called_once_with(
            """
            INSERT INTO cars (brand, model, generation, price, year, mileage, country, region)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            ('Toyota', 'Camry', 'X', 25000.0, 2022, 15000.0, 'Japan', 'Asia')
        )

        # Проверяем, что метод fetchall был вызван у mock_cursor
        mock_cursor.fetchall.assert_called_once()


if __name__ == '__main__':
    main()
