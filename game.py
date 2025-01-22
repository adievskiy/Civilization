import random

import board
import buildings
import great_person
import pers
from pers import Player
from city import City

players_colors = ('Красный', 'Зеленый', 'Синий', 'Желтый')
nations_list = ('Американцы', 'Египтяне', 'Китайцы', 'Немцы', 'Римляне', 'Русские')
painter = []
builder = []
general = []
humanist = []
industrialist = []
scientist = []

# Ввод имени
player_name = input("Введите имя: ")

# Выбор цвета из списка
while True:
    player_color = input("Здравствуйте, {}. Выберите цвет {}: "
                         .format(player_name, players_colors))

    if player_color in players_colors:
        print("{}, вы выбрали {} цвет."
              .format(player_name, player_color))
        break
    else:
        print("Такого цвета нет в списке. Попробуйте снова.")

# Выбор нации из списка
while True:
    player_nation = input("{}, теперь выберите нацию {}: "
                          .format(player_name, nations_list))

    if player_nation in nations_list:
        print("{}, вы выбрали нацию \"{}\"."
              .format(player_name, player_nation))
        break
    else:
        print("Такой нации нет в списке. Попробуйте снова.")

# Создание игрока и стартового поля
player = Player(player_name, player_color, player_nation)
start = board.create_start_square(player_nation)

# Размещение столицы
while True:
    try:
        # Запрос позиции по горизонтали
        x_position = int(input("Выберите стартовую позицию по горизонтали (0-3): "))
        if x_position not in range(0, 4):
            print("Введите цифру от 0 до 3")
            continue

        # Запрос позиции по вертикали
        y_position = int(input("Выберите стартовую позицию по вертикали (0-3): "))
        if y_position not in range(0, 4):
            print("Введите цифру от 0 до 3")
            continue

        player.capital = City(True, x_position, y_position)
        board.place_city(start, x_position, y_position)

        for coord, data in sorted(start.items()):
            print(f"Клетка {coord}: {data}")
        break

    except ValueError:
        print("Введите корректное число")

# Присвоение бонусов нации
print("Стартовые бонусы Вашей нации:")
if player.nation == 'Американцы':

        # Случайный выбор оператора
    person_list = ('painter', 'builder', 'general', 'humanist', 'industrialist', 'scientist')
    random_person = random.choice(person_list)

    if random_person == 'painter':
        print('Вы получаете Великого художника. Он добавляет Вам +1 к торговле и +2 к культуре')
        great_person.stand_and_create_great(player, player.capital, painter, len(painter), random_person)
        pers.player_info(player)

    elif random_person == 'builder':
        print("Вы получаете Великого строителя. Он добавляет Вам +1 к золотым монетам и +2 к промышленности")
        great_person.stand_and_create_great(player, player.capital, builder, len(builder), random_person)
        pers.player_info(player)

    elif random_person == 'general':
        print("Вы получаете Великого генерала. Он добавляет Вам +1 к боевой силе")
        great_person.stand_and_create_great(player, player.capital, general, len(general), random_person)
        pers.player_info(player)

    elif random_person == 'humanist':
        print(
                "Вы получаете Великого гуманиста. Он добавляет Вам +1 к золотым монетам, +1 к промышленности, +1 к торговле и +1 к культуре")
        great_person.stand_and_create_great(player, player.capital, humanist, len(humanist), random_person)
        pers.player_info(player)

    elif random_person == 'industrialist':
        print("Вы получаете Великого промышленника. Он добавляет Вам +1 к золотым монетам, и +2 к культуре")
        great_person.stand_and_create_great(player, player.capital, industrialist, len(industrialist), random_person)
        pers.player_info(player)

    elif random_person == 'scientist':
        print("Вы получаете Великого ученого. Он добавляет Вам +1 к промышленности и +2 к торговле")
        great_person.stand_and_create_great(player, player.capital, scientist, len(scientist), random_person)
        pers.player_info(player)
elif player.nation == 'Египтяне':

    random_wonder = random.choice(buildings.ancient_wonders)

    if random_wonder == 'HangingGardens':
        print("Вы получаете Висячие Сады. В начале хода бесплатно создайте фишку. Она входит в игру на квадрате с Висячими садами.")

    if random_wonder == 'Colossus':
        print("Вы получаете Колосс. В начале хода получите +3 торговли")

    if random_wonder == 'Oracle':
        print("Вы получаете Оракула. В битве ваш противник сразу раскрывает карточки отрядов, с которыми вступает в битву.")

    if random_wonder == 'Stonehenge':
        print("Вы получаете Стоунхедж. В фазе старта получите +1 к культуре.")
elif player.nation == 'Китайцы':
    player.capital_wall = True
elif player.nation == 'Немцы':
    print("Вы получили двух дополнительных пехотинцев")
    player.regular_army['infantry'].extend([random.randint(1, 3), random.randint(1, 3)])
    pers.army_info(player)
elif player.nation == 'Римляне':
    player.government = 'Республика'
elif player.nation == 'Русские':
    player.army_count += 1
    player.government = 'Коммунизм'