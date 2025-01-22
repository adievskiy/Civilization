# Шаг 1: Создаем один квадрат 4x4
def germany_square():
    return {
        (0, 0): {"type": "water", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": "silk"},
        (0, 1): {"type": "plane", "production": 0, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (0, 2): {"type": "water", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (0, 3): {"type": "water", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (1, 0): {"type": "plane", "production": 0, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (1, 1): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (1, 2): {"type": "plane", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (1, 3): {"type": "water", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (2, 0): {"type": "forest", "production": 2, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (2, 1): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (2, 2): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": "iron"},
        (2, 3): {"type": "forest", "production": 2, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (3, 0): {"type": "mountain", "production": 1, "trade": 0, "coin": 1, "culture": 0, "resources": None},
        (3, 1): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (3, 2): {"type": "plane", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (3, 3): {"type": "plane", "production": 0, "trade": 0, "coin": 0, "culture": 0, "resources": "wheat"},
    }

def american_square():
    return {
        (0, 0): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": "iron"},
        (0, 1): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (0, 2): {"type": "water", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (0, 3): {"type": "plane", "production": 0, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (1, 0): {"type": "forest", "production": 2, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (1, 1): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": "silk"},
        (1, 2): {"type": "plane", "production": 0, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (1, 3): {"type": "water", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (2, 0): {"type": "plane", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (2, 1): {"type": "plane", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (2, 2): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": "aroma"},
        (2, 3): {"type": "forest", "production": 2, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (3, 0): {"type": "water", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (3, 1): {"type": "plane", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (3, 2): {"type": "water", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (3, 3): {"type": "forest", "production": 2, "trade": 0, "coin": 0, "culture": 0, "resources": "wheat"},
    }

def romanian_square():
    return {
        (0, 0): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (0, 1): {"type": "plane", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": "aroma"},
        (0, 2): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (0, 3): {"type": "forest", "production": 2, "trade": 0, "coin": 0, "culture": 0, "resources": "silk"},
        (1, 0): {"type": "water", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (1, 1): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (1, 2): {"type": "plane", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (1, 3): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": "iron"},
        (2, 0): {"type": "forest", "production": 2, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (2, 1): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (2, 2): {"type": "plane", "production": 0, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (2, 3): {"type": "water", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (3, 0): {"type": "water", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": "wheat"},
        (3, 1): {"type": "forest", "production": 2, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (3, 2): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (3, 3): {"type": "water", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
    }

def egyptian_square():
    return {
        (0, 0): {"type": "forest", "production": 2, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (0, 1): {"type": "water", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (0, 2): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (0, 3): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": "aroma"},
        (1, 0): {"type": "plane", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": "wheat"},
        (1, 1): {"type": "plane", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": "silk"},
        (1, 2): {"type": "plane", "production": 0, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (1, 3): {"type": "plane", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (2, 0): {"type": "plane", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (2, 1): {"type": "forest", "production": 2, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (2, 2): {"type": "plane", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (2, 3): {"type": "plane", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (3, 0): {"type": "plane", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (3, 1): {"type": "forest", "production": 2, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (3, 2): {"type": "water", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": "silk"},
        (3, 3): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": None},
    }

def chinese_square():
    return {
        (0, 0): {"type": "plain", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (0, 1): {"type": "plain", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (0, 2): {"type": "plain", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (0, 3): {"type": "plain", "production": 0, "trade": 0, "coin": 0, "culture": 0, "resources": "wheat"},
        (1, 0): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": "iron"},
        (1, 1): {"type": "plain", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (1, 2): {"type": "plain", "production": 0, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (1, 3): {"type": "plain", "production": 0, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (2, 0): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (2, 1): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (2, 2): {"type": "forest", "production": 2, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (2, 3): {"type": "forest", "production": 2, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (3, 0): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 1, "resources": None},
        (3, 1): {"type": "water", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (3, 2): {"type": "forest", "production": 2, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (3, 3): {"type": "water", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": "silk"},
    }

def russian_square():
    return {
        (0, 0): {"type": "water", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (0, 1): {"type": "water", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (0, 2): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (0, 3): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (1, 0): {"type": "plain", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (1, 1): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (1, 2): {"type": "plain", "production": 0, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (1, 3): {"type": "water", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (2, 0): {"type": "plane", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (2, 1): {"type": "forest", "production": 2, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (2, 2): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (2, 3): {"type": "water", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (3, 0): {"type": "forest", "production": 2, "trade": 0, "coin": 0, "culture": 0, "resources": "wheat"},
        (3, 1): {"type": "plain", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (3, 2): {"type": "plain", "production": 0, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (3, 3): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": "iron"},
    }

def create_start_square(player_nation):
    # Создаем стартовый квадрат
    if player_nation == 'Американцы':
        start_square = american_square()
    elif player_nation == 'Египтяне':
        start_square = egyptian_square()
    elif player_nation == 'Китайцы':
        start_square = chinese_square()
    elif player_nation == 'Немцы':
        start_square = germany_square()
    elif player_nation == 'Римляне':
        start_square = romanian_square()
    elif player_nation == 'Русские':
        start_square = russian_square()
    else:
        raise ValueError("Неизвестная нация: {}"
                         .format(player_nation))

    return start_square

def place_city(game_field, x, y):
    if (x, y) in game_field:
        game_field[(x, y)]["город"] = True
        print("Город размещен в клетке ({}, {})."
              .format(x, y))
    else:
        print("Клетка ({}, {}) не существует на поле."
              .format(x, y))