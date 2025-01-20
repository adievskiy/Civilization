class Painter:

    def __init__(self, x_position, y_position):
        self.culture_points = 2
        self.trade_points = 1
        self.position = [x_position, y_position]

    def chooses_painter(self, person):
        person.painter_count += 1
        person.culture_points += self.culture_points
        person.trade_points += self.trade_points


class Builder:

    def __init__(self, x_position, y_position):
        self.coin_points = 1
        self.position = [x_position, y_position]

    def chooses_builder(self, person):
        person.builder_count += 1
        person.coin_points += self.coin_points

class General:

    def __init__(self):
        self.war_power = 1

    def chooses_general(self, person):
        person.general_count += 1
        person.war_power += self.war_power

class Humanist:

    def __init__(self):
        self.culture_points = 1
        self.trade_points = 1
        self.production_points = 1
        self.coin_points = 1

    def chooses_humanist(self, person):
        person.humanist_count += 1
        person.culture_points += self.culture_points
        person.trade_points += self.trade_points
        person.production_points += self.production_points
        person.coin_points += self.coin_points

class Industrialist:

    def __init__(self):
        self.culture_points = 2
        self.coin_points = 1

    def chooses_industrialist(self, person):
        person.industrialist_count += 1
        person.culture_points += self.culture_points
        person.coin_points += self.coin_points

class Scientist:

    def __init__(self):
        self.production_points = 1
        self.trade_points = 2

    def chooses_scientist(self, person):
        person.scientist_count += 1
        person.trade_points += self.trade_points
        person.production_points += self.production_points