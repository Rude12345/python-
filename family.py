from termcolor import cprint
from random import randint


class Human:
    def __init__(self, name, house):
        self.name = name
        self.fullness = 30
        self.happiness = 100
        self.house = house
        self.house.residents.append(self)
        self.total_money = 0
        self.total_food = 0
        self.total_mud = 0

    def eat(self):
        cprint('{} ест'.format(self.name))
        self.house.count_food_in_refrigerator -= 30
        self.fullness += 30

    def stroking_a_cat(self):
        self.happiness += 5
        cprint('{} гладит кота'.format(self.name))

    def __str__(self):
        return '{}: Сытость {}, уровень счастья {}'.format(self.name, self.fullness, self.happiness)


class House:
    def __init__(self):
        self.count_money_in_nightstand = 100
        self.count_food_in_refrigerator = 50
        self.count_mud = 0
        self.food_for_cat = 30
        self.residents = list()

    def __str__(self):
        return 'В доме осталось {} денег и {} еды. Дом загрянен на {}%'.format(
            self.count_money_in_nightstand, self.count_food_in_refrigerator, self.count_mud)


class Husband(Human):
    def work(self):
        cprint('{} целый день работал...'.format(self.name), color='cyan')
        self.happiness -= 10
        self.fullness -= 10
        self.house.count_money_in_nightstand += 150
        self.total_money += 150

    def gets_cat(self, pet):
        self.house.residents.append(pet)

    def gaming(self):
        cprint('{} целый день играл...'.format(self.name), color='cyan')
        self.fullness -= 10
        self.happiness += 20

    def act(self):
        if self.happiness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        if self.house.count_mud > 90:
            self.happiness -= 10
        dice = randint(1, 6)
        if self.fullness <= 10:
            self.eat()
        elif self.house.count_money_in_nightstand <= 50:
            self.work()
        elif self.happiness <= 10:
            self.gaming()
        elif dice == 1:
            self.gaming()
        elif dice == 2:
            self.stroking_a_cat()


class Wife(Human):
    def __init__(self, name, house):
        super().__init__(name, house)
        self.coat = 0

    def shopping(self):
        if self.house.count_money_in_nightstand >= 50:
            if self.house.count_food_in_refrigerator <= 30:
                self.house.count_money_in_nightstand -= 30
                self.house.count_food_in_refrigerator += 30
                self.fullness -= 10
                self.total_food += 30
                cprint('{} сходила за продуктами'.format(self.name), color='green')

    def buy_fur_coat(self):
        if self.house.count_money_in_nightstand >= 350:
            self.house.count_money_in_nightstand -= 350
            self.happiness += 60
            self.coat += 1
            cprint('{} купила шубу, вернулась в 90-ые года, так как только тогда это было модно'.format(
                self.name), color='green')
        else:
            cprint('Нет денег на шубу', color='green')
        self.house.count_money_in_nightstand -= 350
        self.happiness += 60
        self.coat += 1
        cprint('{} купила шубу, вернулась в 90-ые года, так как только тогда это было модно'.format(
            self.name), color='green')

    def buy_cat_food(self):
        if self.house.count_money_in_nightstand >= 50:
            if self.house.food_for_cat < 20:
                self.house.count_money_in_nightstand -= 50
                self.house.food_for_cat += 50
                self.total_food += 50
        cprint('{} сходил в магазин за едой для кота'.format(self.name), color='green')

    def clean_house(self):
        cprint('{} занялась уборкой'.format(self.name), color='green')
        self.fullness -= 10
        self.house.count_mud -= 100

    def act(self):
        if self.happiness <= 0:
            cprint('{} умерла...'.format(self.name), color='red')
            return
        if self.fullness <= 0:
            cprint('{} умерла...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness <= 10:
            self.eat()
        elif self.house.count_mud >= 100:
            self.clean_house()
        elif self.house.food_for_cat <= 10:
            self.buy_cat_food()
        elif self.house.count_food_in_refrigerator <= 50:
            self.shopping()
        elif self.happiness <= 10:
            self.buy_fur_coat()
        elif dice == 3:
            self.stroking_a_cat()


class Cat:
    def __init__(self, name, house):
        self.name = name
        self.cat_fullness = 30
        self.house = house

    def __str__(self):
        return '{}: сытость {}'.format(self.name,
                                       self.cat_fullness)

    def eat(self):
        if self.house.food_for_cat >= 10:
            if self.cat_fullness <= 10:
                self.cat_fullness += 20
                self.house.food_for_cat -= 10
            cprint('{} поел'.format(self.name), color='magenta')
        else:
            cprint('Нет кошачьего корма для {}'.format(self.name), color='red')

    def sleep(self):
        cprint('{} лег спать'.format(self.name), color='magenta')
        self.cat_fullness -= 10

    def soil(self):
        cprint('{} дерет обои'.format(self.name), color='magenta')
        self.house.count_mud += 5
        self.cat_fullness -= 10

    def act(self):
        if self.cat_fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 4)
        if self.cat_fullness <= 10:
            self.eat()
        elif dice == 4:
            self.sleep()
        else:
            self.soil()


class Child(Human):
    def __init__(self, name, house):
        super().__init__(name, house)
        self.happiness = 100

    def eat(self):
        if self.house.count_food_in_refrigerator >= 10:
            self.fullness += 10
            self.house.count_food_in_refrigerator -= 10
        cprint('{} не может оторваться от сосуда и все сосет молоко'.format(self.name), color='blue')

    def sleep(self):
        self.fullness -= 5
        cprint('{} сладко сопит'.format(self.name), color='blue')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер ...'.format(self.name), color='red')
            return
        if self.fullness < 20:
            self.eat()
        dice = randint(1, 3)
        if dice == 2:
            self.sleep()


colors = ['cyan', 'green', 'blue', 'magenta', 'magenta', 'magenta']
home = House()
pet_in_home = [Cat(name='Мурзик', house=home),
               Cat(name='Тони', house=home),
               ]

kile = Husband(name='Давид', house=home)
sara = Wife(name='Сара', house=home)
john = Child(name='Джон', house=home)
for i in pet_in_home:
    print(i)
    kile.gets_cat(i)

for day in range(0, 365):
    cprint('================== День {} =================='.format(day), color='red')
    home.count_mud += 5
    if day == 100:
        sara.buy_fur_coat()
    for resident, color in zip(home.residents, colors):
        resident.act()
        cprint(resident, color=color)
    cprint(home, color='grey')
cprint('Итоги года:\n Заработано денег - {}\n Еды съедено - {}\n Шуб куплено - {}'.format(
    kile.total_money, sara.total_food - home.count_food_in_refrigerator, sara.coat
))