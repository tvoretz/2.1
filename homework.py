# -*- coding: utf-8 -*-


def read_cookbook():
    cook_book = {}
    with open('cookbook.txt') as f:
        for line in f:
            dish_name = line.strip().lower()
            ingridients_num = int(f.readline().strip())
            cook_book[dish_name] = []

            for i in range(ingridients_num):
                ingridient_list = f.readline().strip().split(' | ')
                cook_book[dish_name].append({'ingridient_name': ingridient_list[0], 'quantity': int(ingridient_list[1]), 'measure': ingridient_list[2]})
            f.readline()

    print(cook_book)
    return cook_book


def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list_item = dict(ingridient)

            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'],
                                shop_list_item['measure']))


def create_shop_list():
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
        .lower().split(', ')
    cook_book = read_cookbook()
    shop_list = get_shop_list_by_dishes(dishes, person_count, cook_book)
    print_shop_list(shop_list)


create_shop_list()
