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

def square_01():
    return {
        (0, 0): {"type": "plain", "production": 0, "trade": 0, "coin": 0, "culture": 0, "resources": None, "village": True},
        (0, 1): {"type": "plain", "production": 0, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (0, 2): {"type": "forest", "production": 2, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (0, 3): {"type": "forest", "production": 2, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (1, 0): {"type": "desert", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (1, 1): {"type": "plain", "production": 0, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (1, 2): {"type": "forest", "production": 2, "trade": 0, "coin": 0, "culture": 0, "resources": "wheat"},
        (1, 3): {"type": "forest", "production": 2, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (2, 0): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (2, 1): {"type": "water", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (2, 2): {"type": "water", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (2, 3): {"type": "plain", "production": 0, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (3, 0): {"type": "desert", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None, "hut": True},
        (3, 1): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 1, "resources": None},
        (3, 2): {"type": "water", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (3, 3): {"type": "plain", "production": 0, "trade": 0, "coin": 0, "culture": 0, "resources": None},
    }

def square_02():
    return {
        (0, 0): {"type": "desert", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (0, 1): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": None, "hut": True},
        (0, 2): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (0, 3): {"type": "desert", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (1, 0): {"type": "desert", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (1, 1): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (1, 2): {"type": "desert", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (1, 3): {"type": "plain", "production": 0, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (2, 0): {"type": "desert", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": "aroma"},
        (2, 1): {"type": "desert", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (2, 2): {"type": "plain", "production": 0, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (2, 3): {"type": "water", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (3, 0): {"type": "desert", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (3, 1): {"type": "desert", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (3, 2): {"type": "plain", "production": 0, "trade": 0, "coin": 0, "culture": 0, "resources": None, "hut": True},
        (3, 3): {"type": "forest", "production": 2, "trade": 0, "coin": 0, "culture": 0, "resources": None},
    }

def square_03():
    return {
        (0, 0): {"type": "desert", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (0, 1): {"type": "plain", "production": 0, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (0, 2): {"type": "water", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (0, 3): {"type": "water", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (1, 0): {"type": "desert", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (1, 1): {"type": "plain", "production": 0, "trade": 0, "coin": 0, "culture": 0, "resources": None, "village": True},
        (1, 2): {"type": "forest", "production": 2, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (1, 3): {"type": "forest", "production": 2, "trade": 1, "coin": 0, "culture": 0, "resources": "wheat"},
        (2, 0): {"type": "mountain", "production": 1, "trade": 0, "coin": 1, "culture": 0, "resources": None},
        (2, 1): {"type": "desert", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (2, 2): {"type": "plain", "production": 0, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (2, 3): {"type": "forest", "production": 2, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (3, 0): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (3, 1): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (3, 2): {"type": "plain", "production": 0, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (3, 3): {"type": "plain", "production": 0, "trade": 0, "coin": 0, "culture": 0, "resources": None, "hut": True}
    }

def square_04():
    return {
        (0, 0): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": "iron"},
        (0, 1): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (0, 2): {"type": "plain", "production": 0, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (0, 3): {"type": "water", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (1, 0): {"type": "desert", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (1, 1): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (1, 2): {"type": "forest", "production": 2, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (1, 3): {"type": "plain", "production": 0, "trade": 0, "coin": 0, "culture": 0, "resources": None, "hut": True},
        (2, 0): {"type": "desert", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None, "village": True},
        (2, 1): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (2, 2): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (2, 3): {"type": "plain", "production": 2, "trade": 0, "coin": 0, "culture": 1, "resources": None},
        (3, 0): {"type": "desert", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (3, 1): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (3, 2): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (3, 3): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": None}
    }

def square_05():
    return {
        (0, 0): {"type": "desert", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (0, 1): {"type": "desert", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (0, 2): {"type": "plain", "production": 0, "trade": 0, "coin": 0, "culture": 0, "resources": None, "hut": True},
        (0, 3): {"type": "plain", "production": 0, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (1, 0): {"type": "desert", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (1, 1): {"type": "forest", "production": 2, "trade": 0, "coin": 0, "culture": 0, "resources": "aroma"},
        (1, 2): {"type": "forest", "production": 2, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (1, 3): {"type": "plain", "production": 0, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (2, 0): {"type": "water", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (2, 1): {"type": "water", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (2, 2): {"type": "water", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (2, 3): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (3, 0): {"type": "plain", "production": 0, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (3, 1): {"type": "plain", "production": 0, "trade": 0, "coin": 0, "culture": 0, "resources": None, "hut": True},
        (3, 2): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (3, 3): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": None},
    }

def square_06():
    return {
        (0, 0): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": "silk"},
        (0, 1): {"type": "forest", "production": 2, "trade": 0, "coin": 0, "culture": 0, "resources": None, "hut": True},
        (0, 2): {"type": "water", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (0, 3): {"type": "water", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (1, 0): {"type": "plain", "production": 0, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (1, 1): {"type": "plain", "production": 0, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (1, 2): {"type": "water", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (1, 3): {"type": "forest", "production": 2, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (2, 0): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (2, 1): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (2, 2): {"type": "plain", "production": 0, "trade": 0, "coin": 0, "culture": 0, "resources": None, "hut": True},
        (2, 3): {"type": "forest", "production": 2, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (3, 0): {"type": "desert", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (3, 1): {"type": "desert", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (3, 2): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (3, 3): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": None},
    }

def square_07():
    return {
        (0, 0): {"type": "water", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (0, 1): {"type": "water", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (0, 2): {"type": "water", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": "silk"},
        (0, 3): {"type": "water", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (1, 0): {"type": "water", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (1, 1): {"type": "water", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (1, 2): {"type": "plain", "production": 0, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (1, 3): {"type": "forest", "production": 2, "trade": 0, "coin": 0, "culture": 0, "resources": None, "hut": True},
        (2, 0): {"type": "water", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (2, 1): {"type": "plain", "production": 0, "trade": 0, "coin": 0, "culture": 0, "resources": None, "village": True},
        (2, 2): {"type": "forest", "production": 2, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (2, 3): {"type": "forest", "production": 2, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (3, 0): {"type": "plain", "production": 0, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (3, 1): {"type": "forest", "production": 2, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (3, 2): {"type": "forest", "production": 2, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (3, 3): {"type": "desert", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
    }

def square_08():
    return {
        (0, 0): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (0, 1): {"type": "desert", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (0, 2): {"type": "plain", "production": 0, "trade": 0, "coin": 0, "culture": 0, "resources": None, "village": True},
        (0, 3): {"type": "plain", "production": 0, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (1, 0): {"type": "desert", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (1, 1): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (1, 2): {"type": "plain", "production": 0, "trade": 0, "coin": 0, "culture": 1, "resources": None},
        (1, 3): {"type": "forest", "production": 2, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (2, 0): {"type": "desert", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (2, 1): {"type": "plain", "production": 0, "trade": 0, "coin": 0, "culture": 0, "resources": "aroma"},
        (2, 2): {"type": "forest", "production": 2, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (2, 3): {"type": "forest", "production": 2, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (3, 0): {"type": "desert", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (3, 1): {"type": "desert", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None, "hut": True},
        (3, 2): {"type": "desert", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (3, 3): {"type": "desert", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
    }

def square_09():
    return {
        (0, 0): {"type": "forest", "production": 2, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (0, 1): {"type": "water", "production": 0, "trade": 1, "coin": 0, "culture": 1, "resources": None},
        (0, 2): {"type": "forest", "production": 2, "trade": 0, "coin": 0, "culture": 0, "resources": "wheat"},
        (0, 3): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": None, "village": True},
        (1, 0): {"type": "forest", "production": 2, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (1, 1): {"type": "water", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (1, 2): {"type": "water", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (1, 3): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (2, 0): {"type": "forest", "production": 2, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (2, 1): {"type": "plain", "production": 0, "trade": 0, "coin": 0, "culture": 0, "resources": None, "hut": True},
        (2, 2): {"type": "water", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (2, 3): {"type": "forest", "production": 2, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (3, 0): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (3, 1): {"type": "forest", "production": 2, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (3, 2): {"type": "water", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (3, 3): {"type": "forest", "production": 2, "trade": 0, "coin": 0, "culture": 0, "resources": None},
    }

def square_10():
    return {
        (0, 0): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": "aroma"},
        (0, 1): {"type": "desert", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (0, 2): {"type": "desert", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (0, 3): {"type": "water", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (1, 0): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (1, 1): {"type": "plain", "production": 0, "trade": 0, "coin": 0, "culture": 0, "resources": None, "village": True},
        (1, 2): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (1, 3): {"type": "water", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (2, 0): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (2, 1): {"type": "forest", "production": 2, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (2, 2): {"type": "plain", "production": 0, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (2, 3): {"type": "water", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (3, 0): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": None, "hut": True},
        (3, 1): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (3, 2): {"type": "forest", "production": 2, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (3, 3): {"type": "water", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
    }

def square_11():
    return {
        (0, 0): {"type": "forest", "production": 2, "trade": 0, "coin": 0, "culture": 0, "resources": "wheat"},
        (0, 1): {"type": "desert", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (0, 2): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (0, 3): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (1, 0): {"type": "mountain", "production": 1, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (1, 1): {"type": "plain", "production": 0, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (1, 2): {"type": "plain", "production": 0, "trade": 0, "coin": 0, "culture": 0, "resources": None, "hut": True},
        (1, 3): {"type": "water", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (2, 0): {"type": "forest", "production": 2, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (2, 1): {"type": "forest", "production": 2, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (2, 2): {"type": "plain", "production": 0, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (2, 3): {"type": "water", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (3, 0): {"type": "forest", "production": 2, "trade": 0, "coin": 0, "culture": 0, "resources": None, "hut": True},
        (3, 1): {"type": "forest", "production": 2, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (3, 2): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (3, 3): {"type": "forest", "production": 2, "trade": 0, "coin": 0, "culture": 0, "resources": None},
    }

def square_12():
    return {
        (0, 0): {"type": "water", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (0, 1): {"type": "plain", "production": 0, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (0, 2): {"type": "water", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (0, 3): {"type": "water", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (1, 0): {"type": "desert", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (1, 1): {"type": "plain", "production": 0, "trade": 0, "coin": 0, "culture": 0, "resources": None, "hut": True},
        (1, 2): {"type": "water", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (1, 3): {"type": "water", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (2, 0): {"type": "desert", "production": 0, "trade": 1, "coin": 0, "culture": 1, "resources": None},
        (2, 1): {"type": "forest", "production": 2, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (2, 2): {"type": "water", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": "silk"},
        (2, 3): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (3, 0): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (3, 1): {"type": "plain", "production": 0, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (3, 2): {"type": "plain", "production": 0, "trade": 0, "coin": 0, "culture": 0, "resources": None, "hut": True},
        (3, 3): {"type": "plain", "production": 0, "trade": 0, "coin": 0, "culture": 0, "resources": None},
    }

def square_13():
    return {
        (0, 0): {"type": "water", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (0, 1): {"type": "water", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (0, 2): {"type": "water", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (0, 3): {"type": "water", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (1, 0): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": "iron"},
        (1, 1): {"type": "plain", "production": 0, "trade": 0, "coin": 0, "culture": 0, "resources": None, "hut": True},
        (1, 2): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (1, 3): {"type": "desert", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (2, 0): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (2, 1): {"type": "forest", "production": 2, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (2, 2): {"type": "plain", "production": 0, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (2, 3): {"type": "desert", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None, "village": True},
        (3, 0): {"type": "water", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (3, 1): {"type": "water", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (3, 2): {"type": "water", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (3, 3): {"type": "water", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": "silk"},
    }

def square_14():
    return {
        (0, 0): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (0, 1): {"type": "water", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (0, 2): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (0, 3): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": "iron"},
        (1, 0): {"type": "desert", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (1, 1): {"type": "mountain", "production": 1, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (1, 2): {"type": "water", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (1, 3): {"type": "plain", "production": 0, "trade": 0, "coin": 0, "culture": 0, "resources": None, "hut": True},
        (2, 0): {"type": "forest", "production": 2, "trade": 0, "coin": 0, "culture": 0, "resources": None, "hut": True},
        (2, 1): {"type": "desert", "production": 0, "trade": 1, "coin": 0, "culture": 0, "resources": None},
        (2, 2): {"type": "plain", "production": 0, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (2, 3): {"type": "forest", "production": 2, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (3, 0): {"type": "forest", "production": 2, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (3, 1): {"type": "plain", "production": 0, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (3, 2): {"type": "forest", "production": 2, "trade": 0, "coin": 0, "culture": 0, "resources": None},
        (3, 3): {"type": "forest", "production": 2, "trade": 0, "coin": 0, "culture": 0, "resources": None},
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

# def collect_resources(player, game_field, x, y):
#
#     # Список всех возможных соседних клеток (8 направлений)
#     neighbors_square = [
#         (x - 1, y - 1), (x - 1, y), (x - 1, y + 1),
#         (x, y - 1),                 (x, y + 1),
#         (x + 1, y - 1), (x + 1, y), (x + 1, y + 1),
#     ]
#
#     # Собираем ресурсы с соседних клеток
#     resources_collected = {}
#     for nx, ny in neighbors_square:
#         if (nx, ny) in game_field and "ресурсы" in game_field[(nx, ny)]:
#             resource = game_field[(nx, ny)]["ресурсы"]
#             if resource:
#                 if resource in resources_collected:
#                     resources_collected[resource] += 1
#                 else:
#                     resources_collected[resource] = 1