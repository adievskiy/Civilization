class Player:

    def __init__(self, name, color, nation):
        self.name = name
        self.capital = None
        self.color = color
        self.nation = nation
        self.capital_wall = False
        self.culture_points = 0
        self.trade_points = 0
        self.production_points = 0
        self.coin_points = 0
        self.war_power = 0
        self.painter_count = 0
        self.builder_count = 0
        self.general_count = 0
        self.humanist_count = 0
        self.industrialist_count = 0
        self.scientist_count = 0

    def choose_painter(self, painter):
        painter.chooses_painter(self)

    def choose_builder(self, builder):
        builder.chooses_builder(self)

    def choose_general(self, general):
        general.chooses_general(self)

    def choose_humanist(self, humanist):
        humanist.chooses_humanist(self)

    def choose_industrialist(self, industrialist):
        industrialist.chooses_industrialist(self)

    def choose_scientist(self, scientist):
        scientist.chooses_scientist(self)