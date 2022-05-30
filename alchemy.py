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
        elif isinstance(other, Seaweed):
            return Iodine()
        elif isinstance(other, Sand):
            return Glass()


class Earth:

    def __str__(self):
        return 'Earth'

    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Air):
            return Dust()
        elif isinstance(other, Meteor):
            return Iron()


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


class Meteor:

    def __str__(self):
        return 'Meteor'

    def __add__(self, other):
        if isinstance(other, Earth):
            return Iron()


class Iron:

    def __str__(self):
        return 'Железо'


class Seaweed:

    def __str__(self):
        return 'Seaweed'

    def __add__(self, other):
        if isinstance(other, Fire):
            return Iodine()


class Iodine:

    def __str__(self):
        return 'Йод'


class Sand:

    def __str__(self):
        return 'Seaweed'

    def __add__(self, other):
        if isinstance(other, Fire):
            return Glass()


class Glass:

    def __str__(self):
        return 'Cтекло'


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
print(Earth(), '+', Meteor(), '=', Earth() + Meteor())
print(Fire(), '+', Seaweed(), '=', Fire() + Seaweed())
print(Fire(), '+', Sand(), '=', Fire() + Sand())
