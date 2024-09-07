from math import pi


class Sphere:
    """
    Класс Sphere для представления сферы в
    трёхмерном пространстве
    """

    def __init__(self, radius: int = 1, x: int = 0, y: int = 0, z: int = 0):
        self.radius = radius
        self.x = x
        self.y = y
        self.z = z

    def get_volume(self) -> int | float:
        volume = 4 / 3 * pi * self.radius**3
        return volume

    def get_square(self) -> int | float:
        square = 4 * pi * self.radius**2
        return square

    def get_radius(self) -> int | float:
        return self.radius

    def get_center(self) -> tuple[int | float]:
        return (self.x, self.y, self.z)

    def set_radius(self, new_radius: int | float):
        self.radius = new_radius

    def set_center(self, new_x: int | float, new_y: int | float, new_z: int | float):
        self.x = new_x
        self.y = new_y
        self.z = new_z

    def is_point(
        self, point_x: int | float, point_y: int | float, point_z: int | float
    ) -> bool:
        point_l = (
            (point_x - self.x) ** 2 + (point_y - self.y) ** 2 + (point_z - self.z) ** 2
        )
        return self.radius**2 > point_l


sphere = Sphere()
print(sphere.get_volume())
print(sphere.get_square())
print(sphere.get_radius())
print(sphere.get_center())
print("-" * 15)
sphere.set_radius(3)
print(sphere.get_radius())
print("-" * 15)
sphere.set_center(1, 1, 1)
print(sphere.get_center())
print("-" * 15)
print(sphere.is_point(0.5, 0.5, 0.5))
print(sphere.is_point(4, 0.5, 0.5))
print("-" * 15)
