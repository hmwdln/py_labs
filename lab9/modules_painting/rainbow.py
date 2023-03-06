import simple_draw as sd

sd.resolution = (1600, 900)

def rainbow():
    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                    sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
    
    pos_x = -100
    pos_y = -100

    for i in range(0, 7):
        pos_y -= 10
        sd.circle(center_position = sd.Point(pos_x, pos_y), radius = 1800, color = rainbow_colors[i], width = 15)

rainbow()