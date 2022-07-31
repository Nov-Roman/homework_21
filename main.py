from classes import Store, Shop, Request

store = Store()
shop = Shop()

store_items = {
    "печеньки": 10,
    "чипсы": 10,
    "шоколадки": 10,
    "конфеты": 10,
    "сухарики": 10,
    "газировка": 5,
    "мороженное": 5,
    "суфле": 5
}


def main():
    print('Добро пожаловать!')
    while True:
        user_input = input('Введите ваш запрос. Чтобы завершить работу введите "стоп": ').lower()
        if user_input == "стоп":
            break
        try:
            request = Request(user_input)
            store.items = store_items
            from_ = store if request.from_ == 'склад' else shop
            to = store if request.to == 'склад' else shop
            if request.product in from_.items:
                print(f'Нужный товар есть в пункте {request.from_}')
            else:
                print(f'В пункте {request.from_} нет такого товара')
                continue
            if from_.items[request.product] >= request.amount:
                print(f'Нужное колличество есть в пункте {request.from_}')
            else:
                print(f'В пункте {request.from_} не хватает {request.amount - from_.items[request.product]}')
                continue
            if to.get_free_space >= request.amount:
                print(f'В пункте {request.to} достаточно места')
            else:
                print(f'В пункте {request.to} не хватает {request.amount - to.get_free_space}')
                continue
            if request.to == 'магазин' and to.get_unique_items_count == 5 and request.product not in to.items:
                print("В магазине достаточно уникальных значений")
                continue
            from_.remove(request.product, request.amount)
            print(f'Курьер забрал {request.amount} {request.product} из пункта {request.from_}')
            print(
                f'Курьер везёт {request.amount} {request.product} из пункта {request.from_} в пункт {request.to}')
            to.add(request.product, request.amount)
            print(f'Курьер доставил {request.amount} {request.product} в пункт \"{request.to}\"')
            print("=" * 30)
            print('На складе:')
            for title, count in store.items.items():
                print(f'{title}: {count}')
            print("=" * 30)
            print('В магазине:')
            for title, count in shop.items.items():
                print(f'{title}: {count}')
            print(f"Свободного места {shop.get_free_space}")
            print("=" * 30)
        except Exception as e:
            print(f'Что-то пошло не так! Возникла ошибка {e}. Попробуйте снова.')


if __name__ == "__main__":
    main()
