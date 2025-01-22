class Player:

    def __init__(self, name, color, nation):
        self.name = name
        self.capital = None
        self.capital_wall = False
        self.color = color
        self.nation = nation
        self.government = ''
        self.points = {'culture_points': 0, 'trade_points': 0, 'coin_points': 0, 'war_power': 0}
        self.regular_army = {'infantry': [], 'artillery': [], 'cavalry': [], 'aviation': []}
        self.army_power = {'infantry': 1, 'artillery': 1, 'cavalry': 1, 'aviation': 1}
        self.army_count = 0
        self.scout_count = 0


def player_info(user):
    print("Очки торговли: {}\nБогатство: {}\nОчки культуры: {}\nПромышленность столицы: {}\nВоенная сила: {}"
          .format(user.points['trade_points'], user.points['coin_points'], user.points['culture_points'],
                  user.capital.production_points, user.points['war_power']))


def army_info(user):
    print("Пехота: {}, Артиллерия: {}, Кавалерия: {}, Авиация: {}"
          .format(user.regular_army['infantry'], user.regular_army['artillery'], user.regular_army['cavalry'],
                  user.regular_army['aviation']))
