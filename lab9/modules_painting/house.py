import simple_draw as sd

sd.resolution = (1600, 900)

def house():
    pos_x = 250
    pos_y = -50
    pos_x_1 = 350
    pos_y_1 = 0
    new_pos_1 = 50
    new_pos_2 = 0
    for i in range(1, 10):
        temp_1 = pos_x
        temp_2 = pos_x_1
        if i % 2 == 0:
            temp_1 += 50
            temp_2 += 50
        pos_y += 50
        pos_y_1 += 50
        for k in range(1, 6):
            temp_1 += 100
            temp_2 += 100
            sd.rectangle(left_bottom = sd.Point(temp_1, pos_y), right_top = sd.Point(temp_2, pos_y_1), color = sd.COLOR_ORANGE, width = 0)
            sd.rectangle(left_bottom = sd.Point(temp_1, pos_y), right_top = sd.Point(temp_2, pos_y_1), color = sd.COLOR_WHITE, width = 1)
    
    for j in range(1, 8):
        if j % 2 == 0:
            new_pos_1 += 100
            sd.square(sd.Point(350, new_pos_1), color = sd.COLOR_ORANGE)
        else:
            new_pos_2 += 100
            sd.square(sd.Point(850, new_pos_2), color = sd.COLOR_ORANGE)
        

    sd.rectangle(sd.Point(350, 100), sd.Point(900, 450), sd.COLOR_DARK_ORANGE, 3)
    sd.polygon(point_list=(sd.get_point(300, 450), sd.get_point(625, 550), sd.get_point(950, 450)), color = sd.COLOR_DARK_RED, width = 0)