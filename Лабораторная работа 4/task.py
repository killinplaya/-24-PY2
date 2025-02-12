class SocialNetwork:
    """
    Базовый класс для представления социальной сети.

    Атрибуты:
        name (str): Название социальной сети.
        users_count (int): Количество пользователей в социальной сети.
        _is_active (bool): Приватный атрибут, указывающий, активна ли сеть.

    Методы:
        get_users_count(): Возвращает количество пользователей.
        activate_network(): Активирует социальную сеть.
        deactivate_network(): Деактивирует социальную сеть.
    """

    def __init__(self, name: str, users_count: int) -> None:
        """
        Инициализация объекта социальной сети.

        :param name: Название социальной сети.
        :param users_count: Количество пользователей.
        """
        self.name = name
        self.users_count = users_count
        self._is_active = True  # Приватный атрибут, так как его изменение должно быть контролируемым

    def get_users_count(self) -> int:
        """
        Возвращает количество пользователей.

        :return: Количество пользователей.
        """
        return self.users_count

    def activate_network(self) -> None:
        """
        Активирует социальную сеть.
        """
        self._is_active = True

    def deactivate_network(self) -> None:
        """
        Деактивирует социальную сеть.
        """
        self._is_active = False

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.

        :return: Строковое представление объекта.
        """
        status = "Active" if self._is_active else "Inactive"
        return f"{self.name} ({status}) with {self.users_count} users."

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление объекта.

        :return: Формальное строковое представление объекта.
        """
        return f"SocialNetwork(name='{self.name}', users_count={self.users_count}, is_active={self._is_active})"


class VK(SocialNetwork):
    """
    Дочерний класс для представления социальной сети VK.

    Атрибуты:
        communities_count (int): Количество сообществ в VK.

    Методы:
        create_community(): Создает новое сообщество.
        get_users_count(): Переопределенный метод для учета дополнительных пользователей из сообществ.
    """

    def __init__(self, name: str, users_count: int, communities_count: int) -> None:
        """
        Инициализация объекта VK.

        :param name: Название социальной сети.
        :param users_count: Количество пользователей.
        :param communities_count: Количество сообществ.
        """
        super().__init__(name, users_count)
        self.communities_count = communities_count

    def create_community(self) -> None:
        """
        Создает новое сообщество.
        """
        self.communities_count += 1

    def get_users_count(self) -> int:
        """
        Переопределенный метод для учета дополнительных пользователей из сообществ.

        Причина перегрузки: В VK пользователи могут быть участниками сообществ,
        что увеличивает общее количество активных пользователей.

        :return: Общее количество пользователей, включая участников сообществ.
        """
        return self.users_count + self.communities_count * 100  # Предположим, что каждое сообщество добавляет 100 пользователей

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.

        :return: Строковое представление объекта.
        """
        base_str = super().__str__()
        return f"{base_str} Communities: {self.communities_count}"

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление объекта.

        :return: Формальное строковое представление объекта.
        """
        return f"VK(name='{self.name}', users_count={self.users_count}, communities_count={self.communities_count})"


class Facebook(SocialNetwork):
    """
    Дочерний класс для представления социальной сети Facebook.

    Атрибуты:
        pages_count (int): Количество страниц в Facebook.

    Методы:
        create_page(): Создает новую страницу.
        deactivate_network(): Переопределенный метод для деактивации сети с предупреждением.
    """

    def __init__(self, name: str, users_count: int, pages_count: int) -> None:
        """
        Инициализация объекта Facebook.

        :param name: Название социальной сети.
        :param users_count: Количество пользователей.
        :param pages_count: Количество страниц.
        """
        super().__init__(name, users_count)
        self.pages_count = pages_count

    def create_page(self) -> None:
        """
        Создает новую страницу.
        """
        self.pages_count += 1

    def deactivate_network(self) -> None:
        """
        Переопределенный метод для деактивации сети с предупреждением.

        Причина перегрузки: Facebook требует уведомления пользователей перед деактивацией.

        :return: None
        """
        print("Warning: All users will be notified about the deactivation.")
        super().deactivate_network()

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.

        :return: Строковое представление объекта.
        """
        base_str = super().__str__()
        return f"{base_str} Pages: {self.pages_count}"

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление объекта.

        :return: Формальное строковое представление объекта.
        """
        return f"Facebook(name='{self.name}', users_count={self.users_count}, pages_count={self.pages_count})"


if __name__ == "__main__":
    # Создание объектов
    vk = VK(name="VK", users_count=1000000, communities_count=5000)
    facebook = Facebook(name="Facebook", users_count=2000000, pages_count=10000)

    # Тестирование методов
    print(vk)  # Вывод строкового представления
    print(repr(vk))  # Вывод формального представления
    print(f"Users in VK (including communities): {vk.get_users_count()}")  # Переопределенный метод

    vk.create_community()
    print(f"Communities in VK after creation: {vk.communities_count}")

    print(facebook)
    facebook.deactivate_network()  # Переопределенный метод с предупреждением
