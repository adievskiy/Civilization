class Painter:

    def __init__(self, x_position, y_position):
        self.culture_points = 2
        self.trade_points = 1
        self.production_points = 0
        self.coin_points = 0
        self.war_power = 0
        self.position = [x_position, y_position]

class Builder:

    def __init__(self, x_position, y_position):
        self.coin_points = 1
        self.production_points = 2
        self.culture_points = 0
        self.trade_points = 0
        self.war_power = 0
        self.position = [x_position, y_position]

class General:

    def __init__(self, x_position, y_position):
        self.war_power = 1
        self.culture_points = 0
        self.trade_points = 0
        self.production_points = 0
        self.coin_points = 0
        self.position = [x_position, y_position]

class Humanist:

    def __init__(self, x_position, y_position):
        self.culture_points = 1
        self.trade_points = 1
        self.production_points = 1
        self.coin_points = 1
        self.war_power = 0
        self.position = [x_position, y_position]

class Industrialist:

    def __init__(self, x_position, y_position):
        self.culture_points = 2
        self.coin_points = 1
        self.trade_points = 0
        self.production_points = 0
        self.war_power = 0
        self.position = [x_position, y_position]

class Scientist:

    def __init__(self, x_position, y_position):
        self.production_points = 1
        self.trade_points = 2
        self.culture_points = 0
        self.coin_points = 0
        self.war_power = 0
        self.position = [x_position, y_position]

def stand_and_create_great(user, city, great_person, index, chosen_person):
    index -= 1
    while True:
        try:
            x_position = int(input("Выберем где и как поставить по оси x: "))
            if x_position < 0 or (abs(x_position - city.position[0]) > 1):
                print("Вы можете поставить только рядом со столицей")
                continue
            break
        except ValueError:
            print("Введите корректное число")

    while True:
        try:
            y_position = int(input("Выберем где и как поставить по оси y: "))
            if x_position == city.position[0] and y_position == x_position:
                print("Здесь стоит столица!!!")
                continue

            if y_position < 0 or abs(y_position - user.capital.position[1]) > 1:
                print("Вы можете поставить только рядом со столицей")
                continue

            if chosen_person == 'painter':
                create_painter(great_person, x_position, y_position)

            elif chosen_person == 'builder':
                create_builder(great_person, x_position, y_position)

            elif chosen_person == 'general':
                create_general(great_person, x_position, y_position)

            elif chosen_person == 'humanist':
                create_humanist(great_person, x_position, y_position)

            elif chosen_person == 'industrialist':
                create_industrialist(great_person, x_position, y_position)

            elif chosen_person == 'scientist':
                create_scientist(great_person, x_position, y_position)

            user.capital.production_points += great_person[index].production_points
            user.points['coin_points'] += great_person[index].coin_points
            user.points['trade_points'] += great_person[index].trade_points
            user.points['culture_points'] += great_person[index].culture_points
            user.points['war_power'] += great_person[index].war_power
            break

        except ValueError:
            print("Введите корректное число")

def create_painter(great_person, x_position, y_position):
    if len(great_person) < 3:
        great_person.append(Painter(x_position, y_position))
    else:
        print("Художников больше нет")

def create_builder(great_person, x_position, y_position):
    if len(great_person) < 3:
        great_person.append(Builder(x_position, y_position))
    else:
        print("Строителей больше нет")

def create_general(great_person, x_position, y_position):
    if len(great_person) < 3:
        great_person.append(General(x_position, y_position))
    else:
        print("Генералов больше нет")

def create_humanist(great_person, x_position, y_position):
    if len(great_person) < 3:
        great_person.append(Humanist(x_position, y_position))
    else:
        print("Гуманистов больше нет")

def create_industrialist(great_person, x_position, y_position):
    if len(great_person) < 3:
        great_person.append(Industrialist(x_position, y_position))
    else:
        print("Индустриалистов больше нет")

def create_scientist(great_person, x_position, y_position):
    if len(great_person) < 3:
        great_person.append(Scientist(x_position, y_position))
    else:
        print("Ученых больше нет")