"""
ФИО: [Ваше ФИО]
Группа: [Ваша группа]
Занятие 4.3: Наследование, super(), модификаторы доступа, шаблонный метод
"""

# =====================================================================
# Задание 1
# =====================================================================

class Shape:
    def area(self) -> float:
        raise NotImplementedError


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side: float):
        super().__init__(side, side)


# =====================================================================
# Задание 2
# =====================================================================

class MyClass:
    def __init__(self, protected_val, private_val):
        self._protected_attr = protected_val
        self.__private_attr = private_val

    def print_attributes(self):
        print(f"{self._protected_attr} {self.__private_attr}")

# Механизм name mangling автоматически изменяет имя __private_attr на _MyClass__private_attr, чтобы избежать случайных конфликтов и переопределения этого атрибута в подклассах.


# =====================================================================
# Задание 3
# =====================================================================

class BaseWorker:
    def setup(self):
        print("setup")

    def do_work(self):
        raise NotImplementedError

    def cleanup(self):
        print("cleanup")

    def process(self):
        self.setup()
        self.do_work()
        self.cleanup()


class CustomWorker(BaseWorker):
    def do_work(self):
        print("do_work")


# =====================================================================
# Тесты
# =====================================================================
if __name__ == "__main__":
    rect = Rectangle(5, 4)
    square = Square(6)
    print(rect.area())
    print(square.area())

    obj = MyClass("protected", "private")
    obj.print_attributes()
    print(obj._protected_attr)
    print(obj._MyClass__private_attr)

    worker = CustomWorker()
    worker.process()
