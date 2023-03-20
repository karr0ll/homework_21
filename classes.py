from abc import ABC, abstractmethod


class Storage(ABC):
    def __init__(self, items, capacity):
        self.items = {}
        self.capacity = int(capacity)

    @abstractmethod
    def add(self, item, quantity):
        pass

    @abstractmethod
    def remove(self, item, quantity):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def get_unique_items_count(self, items):
        pass


class Store(Storage):

    def __init__(self):
        self.items = {}
        self.capacity = 100

    def add(self, item, quantity):
        """
        добавляет новый товар в список всех товаров, или увеличивает количество уже существующего
        :param item: название товара
        :param quantity: кол-во
        :return:
        """
        if item in self.items.keys():
            if 0 <= quantity <= self.get_free_space():
                self.items[item] = self.items[item] + quantity
                self.print_add_message(item)
            else:
                self.print_low_capacity_message(item)

        if item not in self.items.keys():
            if 0 <= quantity <= self.get_free_space():
                self.items[item] = quantity
                self.print_add_message(item)
            else:
                self.print_low_capacity_message(item)

    def remove(self, item, quantity):
        """
        уменьшает количество товара в списке всех товаров
        :param item: название товара
        :param quantity: кол-во
        :return:
        """
        if self.items[item] - quantity >= 0:
            self.items[item] = self.items[item] - quantity
        else:
            return (f"недостаточно запасов товара '{item}'.\n"
                    f"Можно переместить {self.items[item]} шт.")

    def get_free_space(self):
        """
        получает кол-во свободных мест на складе
        :return:
        """
        return self.capacity - sum(self.items.values())

    def get_items(self):
        """получает все товары на складе"""
        return self.items

    def get_unique_items_count(self, items):
        """возвращает количество уникальных товаров."""
        all_items = [item for item in items]
        unique_items = set(all_items)
        return len(unique_items)

    def print_add_message(self, item):
        """выводит сообщение о добавлении товара на склад(в список всех товаров)"""
        return print(f"Товар '{item}' добавлен на склад\n")

    def print_low_capacity_message(self, item):
        """
        выводит сообщение о недостаточном свободном месте на складе (capacity)
        :param item: название товара
        :return:
        """
        return print(f"Не хватает места на складе для товара '{item}'\n"
                     f"Свободного места {self.get_free_space()}")


class Shop(Store):
    def __init__(self, item_limit=5):
        super().__init__()
        self.items = {}
        self.capacity = 20
        self._item_limit = item_limit

    def get_item_limit(self):
        return self._item_limit

    def add(self, item, quantity):
        items = self.items
        if self.get_unique_items_count(items) < self._item_limit:
            super().add(item, quantity)
        else:
            print(f"Достингут лимит по количеству товаров.'")

    def remove(self, item, quantity):
        super().remove(item, quantity)

    def get_free_space(self):
        return super().get_free_space()

    def get_items(self):
        return super().get_items()

    def get_unique_items_count(self, items):
        """возвращает количество уникальных товаров."""
        # items = self.items
        return super().get_unique_items_count(items)

    def print_add_message(self, item):
        """выводит сообщение о добавлении товара на склад(в список всех товаров)"""
        return super().print_add_message(item)

    def print_low_capacity_message(self, item):
        """
        выводит сообщение о недостаточном свободном месте на складе (capacity)
        :param item: название товара
        :return:
        """
        return super().print_low_capacity_message(item)

class Request:
    def __init__(self, input_):
        list_of_words = self.split_input(input_)

        self.from_ = list_of_words[4]
        if len(list_of_words) >= 6:
            self.to = list_of_words[6]
        self.quantity = int(list_of_words[1])
        self.item = list_of_words[2]

    def split_input(self, input_):
        return input_.split(" ")
