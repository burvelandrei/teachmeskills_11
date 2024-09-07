class Car:
    """
    Класс для описывающий автомобиль, имеет методы запуска
    и остановка автомомобиля, а также изменяемые атрибуты цвет,
    тип и год выпуска.
    """

    def __init__(self, color: str, type: str, year: str):
        self._color = color
        self.__type = type
        self._year = year

    def start_car(self):
        print("Автомобиль заведён")

    def stop_car(self):
        print("Автомобиль заглушен")

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, new_color: str):
        print(f"Цвет машины изменён на {new_color}")
        self._color = new_color

    @color.deleter
    def color(self):
        print("Удаляем цвет машины")
        del self._color

    @property
    def _type(self):
        return self.__type

    @_type.setter
    def _type(self, new_type: str):
        print(f"Тип машины изменён на {new_type}")
        self.__type = new_type

    @_type.deleter
    def _type(self):
        print("Удаляем тип машины")
        del self.__type

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, new_year: str):
        print(f"Год машины изменён на {new_year}")
        self._year = new_year

    @year.deleter
    def year(self):
        print("Удаляем год машины")
        del self._year


toyota = Car("синяя", "легковая", "1995")
print("-" * 30)
toyota.start_car()
toyota.stop_car()
print("-" * 30)
print(toyota.color)
toyota.color = "красная"
print(toyota.color)
print("-" * 30)
print(toyota._type)
toyota._type = "грузовая"
print(toyota._type)
print("-" * 30)
print(toyota.year)
toyota.year = "2000"
print(toyota.year)
print("-" * 30)
