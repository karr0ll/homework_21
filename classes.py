from abc import ABC, abstractmethod


class Storage(ABC):

    @abstractmethod
    def add(self, item: str, quantity: int) -> None:
        pass

    @abstractmethod
    def remove(self, item: str, quantity: int) -> None:
        pass

    @abstractmethod
    def get_free_space(self) -> int:
        pass

    @abstractmethod
    def get_items(self) -> dict:
        pass

    @abstractmethod
    def get_unique_items_count(self, _items: dict) -> int:
        pass


class Store(Storage):

    def __init__(self):
        self._items = {}
        self.capacity = 100

    def add(self, item: str, quantity: int) -> None:
        """
        Добавляет новый товар в список всех товаров, или увеличивает количество уже существующего
        :param item: название товара
        :param quantity: кол-во
        :return:
        """
        if item in self._items.keys():
            if 0 <= quantity <= self.get_free_space():
                self._items[item] = self._items[item] + quantity
                self.print_add_message(item)
            else:
                self.print_low_capacity_message(item)

        if item not in self._items.keys():
            if 0 <= quantity <= self.get_free_space():
                self._items[item] = quantity
                self.print_add_message(item)
            else:
                self.print_low_capacity_message(item)

    def remove(self, item: str, quantity: int) -> str:
        """
        Уменьшает количество товара в списке всех товаров
        :param item: название товара
        :param quantity: кол-во
        :return:
        """
        if self._items[item] - quantity >= 0:
            self._items[item] = self._items[item] - quantity
        else:
            return (f"недостаточно запасов товара '{item}'.\n"
                    f"Можно переместить {self._items[item]} шт.")

    def get_free_space(self) -> int:
        """
        Получает кол-во свободных мест на складе
        :return:
        """
        return self.capacity - sum(self._items.values())

    def get_items(self) -> dict:
        """Получает все товары на складе"""
        return self._items

    def get_unique_items_count(self, _items: dict) -> int:
        """Возвращает количество уникальных товаров."""
        all_items = [item for item in _items]
        unique_items = set(all_items)
        return len(unique_items)

    def print_add_message(self, item: str) -> None:
        """Выводит сообщение о добавлении товара на склад(в список всех товаров)"""
        return print(f"Товар '{item}' добавлен на склад\n")

    def print_low_capacity_message(self, item: str) -> None:
        """
        Выводит сообщение о недостаточном свободном месте на складе (capacity)
        :param item: название товара
        :return:
        """
        return print(f"Не хватает места на складе для товара '{item}'\n"
                     f"Свободного места {self.get_free_space()}")


class Shop(Store):
    def __init__(self, item_limit: int = 5):
        super().__init__()
        self._items = {}
        self.capacity = 20
        self._item_limit = item_limit

    def get_item_limit(self):
        return self._item_limit

    def add(self, item: str, quantity: int) -> None:
        _items = self._items
        if self.get_unique_items_count(_items) < self._item_limit:
            super().add(item, quantity)
        else:
            print(f"Достингут лимит по количеству товаров.'")

    def remove(self, item: str, quantity: int) -> None:
        super().remove(item, quantity)

    def get_free_space(self) -> int:
        return super().get_free_space()

    def get_items(self) -> dict:
        return super().get_items()

    def get_unique_items_count(self, _items: dict) -> int:
        """Возвращает количество уникальных товаров."""
        # _items = self._items
        return super().get_unique_items_count(_items)

    def print_add_message(self, item: str) -> None:
        """Выводит сообщение о добавлении товара на склад(в список всех товаров)"""
        return super().print_add_message(item)

    def print_low_capacity_message(self, item: str) -> None:
        """
        Выводит сообщение о недостаточном свободном месте на складе (capacity)
        :param item: название товара
        :return:
        """
        return super().print_low_capacity_message(item)


class Request:
    def __init__(self, input_: str) -> None:
        list_of_words = self.split_input(input_)

        self.from_ = list_of_words[4]
        if len(list_of_words) >= 6:
            self.to = list_of_words[6]
        self.quantity = int(list_of_words[1])
        self.item = list_of_words[2]

    def split_input(self, input_: str) -> list:
        return input_.split(" ")

