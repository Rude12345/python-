import simple_draw as sd

sd.resolution = (1200, 600)
background_color = (0, 8, 98)
caption = 'Draw the sky'

N = 20

snowflake_parameters = []

for _ in range(N):
    x = sd.random_number(0, 1200)
    y = sd.random_number(0, 600)
    length = sd.random_number(10, 100)
    #   snowflake_parameters = [[]]
    snowflake_parameters.append([x, y, length])

while True:
    sd.start_drawing()
    for i in range(N):
        snowflake = snowflake_parameters[i]
        x = snowflake[0]
        y = snowflake[1]
        length = snowflake[2]
        point = sd.get_point(x, y)

        sd.snowflake(center=point, color=background_color, length=length)
        # x = x + 20
        x += sd.random_number(-30, 30)
        y -= 10
        snowflake = [x, y, length]
        snowflake_parameters[i] = snowflake
        if y < 0:
            snowflake_parameters[i][1] = 600

        point = sd.get_point(x, y)
        sd.snowflake(center=point, color=sd.COLOR_WHITE, length=length)

    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
