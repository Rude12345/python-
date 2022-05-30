import simple_draw as sd

sd.resolution = (1200, 800)

point_0 = sd.get_point(400, 5)

root_point = sd.get_point(600, 5)


def draw_branches(point, angle, length, color):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length)
    v1.draw(color=sd.COLOR_WHITE)
    next_point = v1.end_point
    next_angle = angle - 30
    next_angle2 = angle + 30
    next_length = length * 0.75
    if length < 6:
        return v1.draw(color=sd.COLOR_WHITE)
    elif length < 10:
        v1.draw(color=sd.COLOR_PURPLE)
    draw_branches(point=next_point, angle=next_angle, length=next_length, color=sd.COLOR_WHITE)
    draw_branches(point=next_point, angle=next_angle2, length=next_length, color=sd.COLOR_WHITE)


draw_branches(point=root_point, angle=90, length=120, color=sd.COLOR_WHITE)

sd.pause()