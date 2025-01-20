class City:

    def __init__(self, capital, x_position, y_position):
        self.capital = capital
        self.position = [x_position, y_position]
        self.production_points = 0

    def chooses_builder(self):
        self.production_points += 2