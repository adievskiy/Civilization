ancient_wonders = ('HangingGardens', 'Colossus', 'Oracle', 'Stonehenge')
middle_ages_wonders = ('PorcelainTower', 'HimejiCastle', 'Louvre', 'AngkorWat')
modern_wonders = ('LibertyStatue', 'PanamaCanal', 'SydneyOpera', 'UnitedNation')

class HangingGardens:

    def __init__(self, x_position, y_position):
        self.position = [x_position, y_position]
        self.type = 'ancient'

class Colossus:

    def __init__(self, x_position, y_position):
        self.position = [x_position, y_position]
        self.type = 'ancient'
        self.trade_points = 3

class Oracle:

    def __init__(self, x_position, y_position):
        self.position = [x_position, y_position]
        self.type = 'ancient'

class Stonehenge:

    def __init__(self, x_position, y_position):
        self.position = [x_position, y_position]
        self.type = 'ancient'
        self.culture_points = 1

class PorcelainTower:

    def __init__(self, x_position, y_position):
        self.position = [x_position, y_position]
        self.type = 'Middle Ages'

class HimejiCastle:

    def __init__(self, x_position, y_position):
        self.position = [x_position, y_position]
        self.type = 'Middle Ages'

class Louvre:

    def __init__(self, x_position, y_position):
        self.position = [x_position, y_position]
        self.type = 'Middle Ages'

class AngkorWat:

    def __init__(self, x_position, y_position):
        self.position = [x_position, y_position]
        self.type = 'Middle Ages'

class LibertyStatue:

    def __init__(self, x_position, y_position):
        self.position = [x_position, y_position]
        self.type = 'Modern'

class PanamaCanal:

    def __init__(self, x_position, y_position):
        self.position = [x_position, y_position]
        self.type = 'Modern'

class SydneyOpera:

    def __init__(self, x_position, y_position):
        self.position = [x_position, y_position]
        self.type = 'Modern'

class UnitedNation:

    def __init__(self, x_position, y_position):
        self.position = [x_position, y_position]
        self.type = 'Modern'