class Car:

    # Инициализация объекта (конструктор)
    def __init__(self, make, model, year,km,motor,wheels):
        self.make = make    # Поле или атрибут класса
        self.model = model  # Поле или атрибут  класса
        self.year = year    # Поле или атрибут класса
        self.km = km
        self.motor = motor
        self.wheels = wheels

    # Метод класса для получения информации о машине
    def info(self):
        return f"{self.year} {self.make} {self.model} {self.km} {self.motor} {self.wheels}"

# Создаем объекты класса Car
car1 = Car("Toyota", "Camry", 2020,)
car2 = Car("Honda", "Civic", 2022)

# Используем методы и атрибуты
print(car1.info())  # Выводит: "2020 Toyota Camry"
print(car2.info())  # Выводит: "2022 Honda Civic"