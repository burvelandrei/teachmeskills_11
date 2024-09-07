class Soda():
    def __init__(self, taste: str|None = None):
        self.taste = taste

    def __str__(self):
        if self.taste is not None:
            return f"У вас газировка с {self.taste} вкусом"
        else:
            return "У вас обычная газировка"


strawberry = Soda("клубничным")
print(strawberry)
no_taste = Soda()
print(no_taste)
orange = Soda("апельсиновым")
print(orange)