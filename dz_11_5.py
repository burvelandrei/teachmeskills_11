class SuperStr(str):
    """
    Класс  расширяющий возможности стандартного класса str,
    добавлена проверка на вхождение переданной строки в текущую
    и проверка на палиндром
    """

    def __init__(self, string: str):
        self.string = string

    def is_repeatance(self, sample: str) -> bool:
        if not len(self.string):
            return False
        count_repeat = len(self.string) // (len(sample) or 1)
        return self.string == sample * count_repeat

    def is_palindrom(self) -> bool:
        return self.string.lower() == self.string.lower()[::-1]


print("-" * 10)
super_str = SuperStr("abc")
print(super_str.is_palindrom())
print("-" * 10)
super_str_2 = SuperStr("abcdeabcde")
print(super_str_2.is_repeatance("abc"))
print(super_str_2.is_repeatance("abcde"))
print("-" * 10)
super_str_3 = SuperStr("")
print(super_str_3.is_repeatance(""))
print("-" * 10)