import simple_draw as sd

starting_point = sd.Point(1200, 0)

sd.resolution = (1600, 900)

def draw_branches(cur_point, cur_angle, cur_length):
    if cur_length < 10:
        return

    first_vector = sd.get_vector(cur_point, cur_angle, cur_length)
    second_vector = sd.get_vector(cur_point, cur_angle, cur_length)
    first_vector.draw()
    second_vector.draw()
    
    exit_point_1 = first_vector.end_point

    next_vector = cur_length * (sd.random_number(60, 90) / 100)

    draw_branches(exit_point_1, cur_angle + sd.random_number(18, 42), next_vector)
    draw_branches(exit_point_1, cur_angle - sd.random_number(18, 42), next_vector)

def tree():
    start_vector = sd.get_vector(starting_point, 90, 100)
    start_vector.draw()
    draw_branches(start_vector.end_point, 90, 100)
