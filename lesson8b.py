from pprint import pprint

goods = [
    {
        'name': 'Iphone 14',
        'brand': 'Apple',
        'price': 1200
    },
    {
        'name': 'Samsung Galaxy A53',
        'brand': 'Samsung',
        'price': 500
    },
    {
        'name': 'Realme c25s',
        'brand': 'Realme',
        'price': 400
    }
]
if __name__ == "__main__":

    #def item_price(item):
    #    return item.get('price')

    #pprint(sorted(goods, key=lambda item: item['price']))

    #apple_list = filter(lambda item: item['brand'] == 'Apple', goods)
    #pprint(list(apple_list))

    # numbers_list = ['1','2','3','4','5','6']
    # numbers_list = list(map(int, numbers_list))
    # print(numbers_list)
    #
    names = ['Иван', 'Пётр', 'Максим']
    surnames = ['Петров', 'Павлов', 'Сидоров']
    patronymics = ['Данилович', 'Николаевич', 'Владиславович']
    # full_names = list(map(lambda name, surname: f'{name} {surname}',names, surnames))
    # print(full_names)

    indexed_goods = []

    # for i, item in enumerate(goods):
    #     indexed_goods.append({i: item})
    # pprint(indexed_goods)

    for name, surname, patronymic in zip(names, surnames, patronymics):
        print(surname, name, patronymic)

    print(__name__)