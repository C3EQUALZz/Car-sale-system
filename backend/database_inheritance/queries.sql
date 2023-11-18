-- Создание таблицы cars
CREATE TABLE IF NOT EXISTS cars (
    id INTEGER PRIMARY KEY,
    brand TEXT,
    model TEXT,
    generation TEXT,
    price REAL,
    year INTEGER,
    mileage INTEGER,
    country TEXT,
    region TEXT
);

-- Создание таблицы orders
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY,
    car_id INTEGER,
    customer_name TEXT,
    order_date TEXT,
    FOREIGN KEY (car_id) REFERENCES cars(id)
);