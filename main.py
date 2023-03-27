from classes import Store, Shop, Request
from constants import WHS_LIST

from utils import check_item_is_on_stock, check_outbound_whs_name, check_query_availability, \
    check_inbound_whs_space, print_items_list

store = Store()
store.items = ({"печеньки": 21,
                "собачки": 10,
                "коробки": 5,
                "вилки": 2,
                "ложки": 3,
                "салфетки": 4})

shop = Shop()

whs_list = WHS_LIST

if __name__ == "__main__":
    while True:
        print(f"Введите место отгрузки {whs_list}:")

        # проверяет наличие введенного склада в списке складов
        from_ = check_outbound_whs_name(whs_list)

        # устанавливает нужный класс объекта
        if from_ == whs_list[0]:
            location_class = store
        else:
            location_class = shop

        # получает направление перемещения (конечный склад)
        items_list = ([key for key in location_class.items])
        while len(items_list) == 0:
            print(f"Склад пуст. Введите новое место отгрузки {whs_list}:")
            from_ = check_outbound_whs_name(whs_list)
            if from_ == whs_list[0]:
                location_class = store
            else:
                location_class = shop
            items_list = ([key for key in location_class.items])

        # печатает список доступных на складе товаров
        print_items_list(location_class, from_)

        # получает ввод названия товара
        print(f"\nВведите товар: {items_list}")
        item = check_item_is_on_stock(items_list)

        while True:
            try:
                quantity = int(input('Введите количество: '))
                break
            except TypeError:
                print("Вы ввели не целое число")
                continue

        if from_ == whs_list[0]:
            to = whs_list[1]
        else:
            to = whs_list[0]

        # формирует строку из пользовательского ввода
        order = f"Доставить {quantity} {item} из {from_} в {to}"
        request = Request(order)
        if request.from_ == whs_list[0]:
            outbound_whs = store
            inbound_whs = shop
        else:
            outbound_whs = shop
            inbound_whs = store

        # проверяет остаток товара на складе
        check_query_availability(request, outbound_whs, request.item)

        # проверяет остаток свободного места на складе назначения
        check_inbound_whs_space(request, inbound_whs, request.to)

        print(f"Задание: {order}")

        # умменьшает количество товара на складе отрузки
        outbound_whs.remove(request.item, request.quantity)
        print_items_list(outbound_whs, from_)

        print(f"\nКурьер забрал {request.quantity} {request.item} из {request.from_}\n"
              f"Курьер везет {request.quantity} {request.item} из {request.from_} в {request.to}\n"
              f"Курьер доставил {request.quantity} {request.item} из {request.from_} в {request.to}\n")

        # увеличивает остаток товара на складе
        inbound_whs.add(request.item, request.quantity)
        print_items_list(inbound_whs, to)
        continue
