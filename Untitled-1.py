from random import choice


def get_hero(name=None,
            hp=100, 
            level=1,
            xp=0, 
            money=25,
            inventory=None
            ) -> list:
    if not name:
        names = ('роман', 'Валера', 'Мао', 'Акакий', 'Вася')
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
        option = input('выберите покупку:')
    #TODO Купить товар по опции

shop_item = ['зелье лечения', 'зелье копчения']
visit_shop(player, shop_item)



player = get_hero('вася')
show_hero(player)

