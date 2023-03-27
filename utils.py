def check_outbound_whs_name(whs_list):
    """
    проверяет введенные данные на наличие в списке складов
    :param whs_list: список складов(константа)
    :return: проверенное значение пользовательского ввода
    """
    from_ = input()
    is_in_whs_list = False
    while from_ not in whs_list:
        from_ = input(f"Такого места отгрузки нет.\nВведите место отгрузки {whs_list}\n")
        if from_ in whs_list:
            is_in_whs_list = True
    return from_


def print_items_list(location_class, destination):
    """
    выводит на печать остатки товаров на складе
    :param location_class: класс Store или Shop
    :param destination: переменная, фиксирующая направление перемещения товара
    :return:
    """
    if len(location_class.items.items()) == 0:
        print(f"На складе '{destination}' нет товаров")
    else:
        print(f"На складе '{destination}' хранится:")
        for key, item in location_class.items.items():
            print(f"{key} - {item} шт.")


def check_item_is_on_stock(items_list):
    """
    проверяет есть ли введенный товар на складе отгрузки
    :param items_list: список всех товаров на складе отгузки
    :return: проверенный ввод пользоватеьских данных
    """
    item = input()
    item_is_in_list = False
    while item not in items_list:
        item = input(f"Такой товар не найден. Введите название товара из списка: {items_list}\n")
        if item in items_list:
            item_is_in_list = True
    return item


def check_query_availability(request, outbound_whs, item):
    """
    проверяет доступный остаток товара на складе отгрузки
    :param request: экземпляр класса Request
    :param outbound_whs: переменная, передающая склад отгрузки
    :param item: запрошенный товар
    :return:
    """
    is_checked = False
    while not is_checked:
        if request.quantity <= outbound_whs.items[item]:
            is_checked = True
        else:
            request.quantity = int(input(f"Запрошенное количество превышает доступный остаток на складе "
                                         f"'{request.from_}'.Доступно {outbound_whs._get_items()[item]}\n"
                                         f"Введите новое количество товара\n"))


def check_inbound_whs_space(request, inbound_whs, to):
    """
    проверяет, есть свободное место на складе отгрузки
    :param request: экземпляр класса Request
    :param inbound_whs: переменная, передающая экземпляр класса Store или Shop в зависимости от контекста
    :param to: строковое выражение названия склада назначения
    :return:
    """
    is_checked = False
    while not is_checked:
        if request.quantity <= inbound_whs.get_free_space():
            is_checked = True
        else:
            request.quantity = int(input(f"Запрошенное количество превышает место на складе '{to}'."
                                         f"Доступно {inbound_whs.get_free_space()}\nВведите новое количество товара\n"))

