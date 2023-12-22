from random import choice


def get_hero(name=None,
            hp=100, 
            level=1,
            xp=0, 
            money=25,
            inventory=None
            ) -> list:
    if not name:
        names = choice(['роман', 'Валера', 'Мао', 'Акакий', 'Вася'])
        name = choice(names)
    if not inventory:
        inventory = []
    return [name,  hp, level, xp, money, inventory]


def show_hero(hero: list) -> None:
    #выводит на экран героя
    print('имя:', hero[0])
    print('жизни:', hero[1])
    print('уровень:', hero[2])
    print('опыт:', hero[3])
    print('деньги:', hero[4])
    print('инвентарь:', hero[5])
print('-' * 10)

player = get_hero('вася')
show_hero(player)


def  visit_shop(hero, shop_item):
    print(f'{hero[0]} приехал в лавку')
    print('1 - купить товары')
    print('2 - продать товары')
    print('0 - выйти')
    option = input('введите номер опции:')
    if option == '1':
        for num, item in enumerate(shop_item, 1):
            print(f'{num} - {item}')
        print('0 - отмена')
        option = int(input('выберите покупку:'))
        prise_tmp = 10
        if option > len(shop_item) or option < 0:
            print('неверная опция')
        elif option == '0':
            print('выход')
        else:
            item_index = int(option) - 1
            item_name = shop_item[item_index]
            if hero[4] < prise_tmp:
                print('нет монет')
            else:
                hero[4] -= prise_tmp
                hero[5].append(item_name)
                shop_item.pop(item_index)
                print(hero[4])
            print(f'{hero[0]} купил {item_name}')
            

shop_item = ['зелье лечения', 'зелье копченият', 'зелье лечения', 'зелье копченият', 'зелье лечения', 'зелье копченият']
visit_shop(player, shop_item)
print('--- игра окончена ---')
show_hero(player)
visit_shop(player, shop_item)

player = get_hero()
show_hero(player)


