import simple_draw as sd

sd.resolution = (1200, 600)


class Snowflake:
    def __init__(self):
        self.color = sd.COLOR_WHITE
        self.length = sd.random_number(10, 100)
        self.x = sd.random_number(0, 1200)
        self.y = sd.random_number(0, 600)

    def clear_previous_picture(self):
        self.color = sd.background_color
        sd.snowflake(center=sd.get_point(self.x, self.y),
                     length=self.length,
                     color=self.color)

    def move(self):
        if self.can_fall():
            self.y -= sd.random_number(0, 10)
            self.x += sd.random_number(0, 15)

    def draw(self):
        self.color = sd.COLOR_WHITE
        sd.snowflake(center=sd.get_point(self.x, self.y), length=self.length, color=self.color)

    def can_fall(self):
        return self.y > 10


N = 25


def get_flakes(count):
    snowflakes = []
    for _ in range(0, count):
        snowflakes.append(Snowflake())
    return snowflakes


def get_fallen_flakes(count):
    count = 0
    for fallen_flakes in flakes:
        if fallen_flakes.y <= 10:
            count += 1
    return count


def append_flakes(snowflakes, count):
    for _ in range(0, N - len(snowflakes)):
        snowflakes.append(Snowflake())
    return count


def remove_flakes(flakes):
    for snow in flakes:
        if snow.y <= 10:
            flakes.remove(snow)
    del snow
    return flakes


flakes = get_flakes(count=N)

while True:
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
    fallen_flakes = get_fallen_flakes(count=N)
    if fallen_flakes:
        remove_flakes(flakes)
    append_flakes(flakes, count=fallen_flakes)
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
