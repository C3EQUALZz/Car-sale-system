"""
Здесь класс, который описывает сущность самой машины.
Для каждого автомобиля должны быть указаны атрибуты, такие как:
марка, модель, поколение, цена, год выпуска, пробег, страна производителя, регион продажи авто.
"""
__all__ = ["Car"]

from dataclasses import dataclass


@dataclass
class Car:
    brand: str
    model: str
    generation: str
    price: float
    year: int
    mileage: float
    country: str
    region: str
