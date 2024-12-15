import abc
from abc import ABC, abstractmethod
import doctest


class AbstractCar(ABC):
    def __init__(self, brand: str, speed: float, seats: int):
        """
        Инициализация объекта "Автомобиль".

        :param brand: Марка автомобиля
        :type brand: str
        :param speed: Скорость автомобиля (км/ч)
        :type speed: float
        :param seats: Количество мест в автомобиле
        :type seats: int

        :raises TypeError: Если типы аргументов неверные.
        :raises ValueError: Если скорость или количество мест не положительны.

        Примеры:
        >>> # car = AbstractCar("Tesla", -10.0, 4) # ValueError, т.к. скорость не может быть отрицательной
        """
        if not isinstance(brand, str):
            raise TypeError("brand должен быть строкой")
        if not isinstance(speed, (int, float)):
            raise TypeError("speed должен быть числом")
        if not isinstance(seats, int):
            raise TypeError("seats должен быть целым числом")

        if speed <= 0:
            raise ValueError("speed должен быть положительным числом")
        if seats <= 0:
            raise ValueError("seats должен быть положительным числом")

        self.brand = brand
        self.speed = speed
        self.seats = seats

    @abstractmethod
    def accelerate(self, delta: float) -> None:
        """
        Увеличивает скорость автомобиля.

        :param delta: Величина увеличения скорости (км/ч)
        :type delta: float

        :raises ValueError: Если delta не положительно.

        Примеры:
        >>> class ConcreteCar(AbstractCar):
        ...     def accelerate(self, delta: float) -> None:
        ...         if delta <= 0:
        ...             raise ValueError("delta должна быть положительной")
        ...         # Реализация не требуется, достаточно заглушки
        ...         ...
        ...     def brake(self) -> None:
        ...         ...
        >>> c = ConcreteCar("Audi", 100.0, 4)
        >>> c.accelerate(20)
        """
        ...

    @abstractmethod
    def brake(self) -> None:
        """
        Применяет торможение.

        Пример использования:
        >>> class ConcreteCar(AbstractCar):
        ...     def accelerate(self, delta: float) -> None:
        ...         ...
        ...     def brake(self) -> None:
        ...         # Реализация не требуется
        ...         ...
        >>> c = ConcreteCar("BMW", 150.0, 4)
        >>> c.brake()
        """
        ...


class AbstractBook(ABC):
    def __init__(self, title: str, pages: int):
        """
        Инициализация объекта "Книга".

        :param title: Название книги
        :type title: str
        :param pages: Количество страниц в книге
        :type pages: int

        :raises TypeError: Если типы аргументов неверные.
        :raises ValueError: Если количество страниц не положительно.

        Примеры:
        >>> # book = AbstractBook("Some Title", 0) # ValueError, т.к. страниц не может быть 0
        """
        if not isinstance(title, str):
            raise TypeError("title должен быть строкой")
        if not isinstance(pages, int):
            raise TypeError("pages должен быть целым числом")

        if pages <= 0:
            raise ValueError("pages должен быть положительным числом")

        self.title = title
        self.pages = pages

    @abstractmethod
    def read_pages(self, count: int) -> None:
        """
        Прочитать указанное количество страниц.

        :param count: Количество страниц для прочтения
        :type count: int

        :raises ValueError: Если count не положительно.

        Примеры:
        >>> class ConcreteBook(AbstractBook):
        ...     def read_pages(self, count: int) -> None:
        ...         if count <= 0:
        ...             raise ValueError("count должен быть положительным")
        ...         ...
        ...     def get_remaining_pages(self) -> int:
        ...         return 100
        >>> b = ConcreteBook("Python 101", 300)
        >>> b.read_pages(10)
        """
        ...

    @abstractmethod
    def get_remaining_pages(self) -> int:
        """
        Возвращает количество оставшихся непрочитанных страниц.

        :return: Количество оставшихся страниц
        :rtype: int

        Примеры:
        >>> class ConcreteBook(AbstractBook):
        ...     def read_pages(self, count: int) -> None:
        ...         ...
        ...     def get_remaining_pages(self) -> int:
        ...         return 250
        >>> b = ConcreteBook("Learning Python", 400)
        >>> b.get_remaining_pages()
        250
        """
        ...


class AbstractServer(ABC):
    def __init__(self, name: str, capacity: int):
        """
        Инициализация объекта "Сервер".

        :param name: Название сервера
        :type name: str
        :param capacity: Максимальная емкость по количеству пользователей
        :type capacity: int

        :raises TypeError: Если типы аргументов неверные.
        :raises ValueError: Если емкость не положительна.

        Примеры:
        >>> # server = AbstractServer("MyServer", 0) # ValueError, т.к. емкость не может быть 0
        """
        if not isinstance(name, str):
            raise TypeError("name должен быть строкой")
        if not isinstance(capacity, int):
            raise TypeError("capacity должен быть целым числом")

        if capacity <= 0:
            raise ValueError("capacity должен быть положительным числом")

        self.name = name
        self.capacity = capacity

    @abstractmethod
    def add_user(self, username: str) -> None:
        """
        Добавляет пользователя на сервер.

        :param username: Имя пользователя
        :type username: str

        :raises ValueError: Если достигнута максимальная емкость или имя пользователя некорректно.

        Примеры:
        >>> class ConcreteServer(AbstractServer):
        ...     def add_user(self, username: str) -> None:
        ...         if not username:
        ...             raise ValueError("username не может быть пустым")
        ...         ...
        ...     def remove_user(self, username: str) -> None:
        ...         ...
        >>> s = ConcreteServer("TestServer", 100)
        >>> s.add_user("user1")
        """
        ...

    @abstractmethod
    def remove_user(self, username: str) -> None:
        """
        Удаляет пользователя с сервера.

        :param username: Имя пользователя для удаления
        :type username: str

        :raises ValueError: Если пользователя с таким именем нет.

        Примеры:
        >>> class ConcreteServer(AbstractServer):
        ...     def add_user(self, username: str) -> None:
        ...         ...
        ...     def remove_user(self, username: str) -> None:
        ...         if username == "unknown":
        ...             raise ValueError("Такого пользователя нет")
        ...         ...
        >>> s = ConcreteServer("MyServer", 50)
        >>> s.remove_user("user1")  # Предположим, что user1 есть
        """
        ...


if __name__ == "__main__":
    doctest.testmod(verbose=True)
