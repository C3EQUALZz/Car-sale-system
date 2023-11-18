from backend.database_inheritance import CarDatabase
from backend.auto_inheritance import Car


if __name__ == "__main__":
    with CarDatabase() as car_db:
        car = Car('Toyota', 'Camry', 'VIII', 25000, 2022, 0, 'Japan', 'Asia')
        car_db.append(car)

        cars = car_db.view_cars()
        for car in cars:
            print(car)

        # Пример удаления машины по ID (замените на реальный ID)
        car_db.pop(1)
