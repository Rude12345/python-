class Water:

    def __str__(self):
        return 'Water'

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Dirt()


class Air:

    def __str__(self):
        return 'Air'

    def add(self, other):
        if isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()


class Fire:

    def __str__(self):
        return 'Fire'

    def __add__(self, other):
        if isinstance(other, Earth):
            return Lava()
        elif isinstance(other, Air):
            return Lightning()


class Earth:

    def __str__(self):
        return 'Earth'

    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Air):
            return Dust()


class Storm:

    def __str__(self):
        return 'Шторм'


class Steam:

    def __str__(self):
        return 'Пар'


class Dirt:

    def __str__(self):
        return 'Грязь'


class Lightning:

    def __str__(self):
        return 'Молния'


class Dust:

    def __str__(self):
        return 'Пыль'


class Lava:

    def __str__(self):
        return 'Лава'


water = Water()
print(water)
air = Air()
print(air)
fire = Fire()
print(fire)
earth = Earth()
print(earth)
print(Water(), '+', Air(), '=', Water() + Air())
print(Water(), '+', Fire(), '=', Water() + Fire())
print(Water(), '+', Earth(), '=', Water() + Earth())
print(Fire(), '+', Air(), '=', Fire() + Air())
print(Earth(), '+', Air(), '=', Earth() + Air())
print(Fire(), '+', Earth(), '=', Fire() + Earth())