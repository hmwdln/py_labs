import simple_draw as sd

def snow():
    N = 20
    i = 1
    snowflakes = []

    for _ in range(N):
        dict_of_snowflakes = {'length': sd.random_number(10, 50), 'x': sd.random_number(0, 300), 'y': 300 + sd.randint(50, 75)}
        snowflakes.append(dict_of_snowflakes)

    sd.start_drawing()

    while True:
        for snowflake in snowflakes:
            point_xy = sd.get_point(snowflake['x'], snowflake['y'])
            sd.snowflake(center=point_xy, color=sd.background_color, length=snowflake['length'])

            snowflake['x'] -= sd.random_number(-5, 15)
            snowflake['y'] -= sd.random_number(5, 30)

            point_xy = sd.get_point(snowflake['x'], snowflake['y'])
            sd.snowflake(center=point_xy, color=sd.COLOR_WHITE, length=snowflake['length'])

            if i % 40 == 0:
                new_snowflake = {'length': sd.random_number(10, 50), 'x': sd.random_number(0, 300), 'y': 300 + sd.randint(50, 75)}
                snowflakes.append(new_snowflake)

            if snowflake['y'] < 150:
                snowflakes.remove(snowflake)

            i += 1
        
        sd.finish_drawing()
        sd.sleep(0.1)

        if sd.user_want_exit():
            break

snow()