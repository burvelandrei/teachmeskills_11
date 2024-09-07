class Math:
    """Класс для реализации некоторых функций калькулятора"""

    def addition(self, number_1: int | float, number_2: int | float):
        try:
            print(number_1 + number_2)
        except TypeError:
            print("Нужно передать числа!")

    def subtraction(self, number_1: int | float, number_2: int | float):
        try:
            print(number_1 - number_2)
        except TypeError:
            print("Нужно передать числа!")

    def multiplication(self, number_1: int | float, number_2: int | float):
        try:
            print(number_1 * number_2)
        except TypeError:
            print("Нужно передать числа!")

    def division(self, number_1: int | float, number_2: int | float):
        try:
            print(number_1 / number_2)
        except ZeroDivisionError:
            print("На ноль делить нельзя!")
        except TypeError:
            print("Нужно передать числа!")


Calc = Math()
Calc.addition(3, 4)
Calc.subtraction(5, 4)
Calc.multiplication(5, 5)
Calc.division(5, 5)
