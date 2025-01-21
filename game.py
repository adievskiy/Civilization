import random

from great_person import Painter, Builder, General, Humanist, Industrialist, Scientist
from player import Player
from city import City

players_colors = ('Красный', 'Зеленый', 'Синий', 'Желтый')
nations_list = ('Китайцы', 'Русские', 'Немцы', 'Американцы', 'Египтяне')
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

# Создание игрока
player = Player(player_name, player_color, player_nation)

# Выбор стартовой позиции столицы
while True:
    try:
        # Запрос позиции по горизонтали
        x_position = int(input("Выберите стартовую позицию по горизонтали (1-4): "))
        if x_position not in range(1, 5):
            print("Введите цифру от 1 до 4")
            continue

        # Запрос позиции по вертикали
        y_position = int(input("Выберите стартовую позицию по вертикали (1-4): "))
        if y_position not in range(1, 5):
            print("Введите цифру от 1 до 4")
            continue

        player.capital = City(True, x_position, y_position)
        break

    except ValueError:
        print("Введите корректное число")

# Присвоение бонусов нации
# Американцам надо добавить размещение человека на поле
"""////////// Американцы не дописаны //////////"""
if player.nation == 'Американцы':
    print("Стартовые бонусы Вашей нации:")

        # Случайный выбор оператора
    person_list = ('painter', 'builder', 'general', 'humanist', 'industrialist', 'scientist')
    chosen_person = random.choice(person_list)

    if chosen_person == 'painter':
        player.choose_painter(painter[0])
        print('Вы получаете Великого художника. Он добавляет Вам +1 к торговле и +2 к культуре')

    elif chosen_person == 'builder':
        print("Вы получаете Великого строителя. Он добавляет Вам +1 к золотым монетам и +2 к промышленности")
        # Размещаем Великого человека
        # Проверяем ввод по оси x
        while True:
            try:
                x_position = int(input("Выберем где и как поставить по оси x: "))
                if x_position < 0 or (abs(x_position - player.capital.position[0]) > 1):
                    print("Вы можете поставить только рядом со столицей")
                    continue
                break
            except ValueError:
                print("Введите корректное число")
        # Проверяем ввод по оси y и создаем экземпляр в builder[0]
        while True:
            try:
                y_position = int(input("Выберем где и как поставить по оси y: "))
                if x_position == player.capital.position[0] and y_position == x_position:
                    print("Здесь стоит столица!!!")
                    continue

                if y_position < 0 or abs(y_position - player.capital.position[1]) > 1:
                    print("Вы можете поставить только рядом со столицей")
                    continue

                builder.append(Builder(x_position, y_position))
                player.choose_builder(builder[0])
                player.capital.production_points += builder[0].production_points
                player.coin_points += builder[0].coin_points
                break

            except ValueError:
                print("Введите корректное число")

    elif chosen_person == 'general':
        player.choose_general(general[0])
        print("Вы получаете Великого генерала. Он добавляет Вам +1 к боевой силе")

    elif chosen_person == 'humanist':
        player.choose_humanist(humanist[0])
        print(
                "Вы получаете Великого гуманиста. Он добавляет Вам +1 к золотым монетам, +1 к промышленности, +1 к торговле и +1 к культуре")

    elif chosen_person == 'industrialist':
        player.choose_industrialist(industrialist[0])
        print("Вы получаете Великого промышленника. Он добавляет Вам +1 к золотым монетам, и +2 к культуре")

    elif chosen_person == 'scientist':
        player.choose_scientist(scientist[0])
        print("Вы получаете Великого ученого. Он добавляет Вам +1 к промышленности и +2 к торговле")