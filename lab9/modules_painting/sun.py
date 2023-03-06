import simple_draw as sd

sd.resolution = (1600, 900)

def draw_sun():
    center_position = sd.get_point(200, 700)
    radius = 100

    sd.circle(center_position, radius, width=0, color=sd.COLOR_YELLOW)

    ray_start_position = sd.get_point(200, 700)
    ray_length = 150

    for angle in range(0, 360, 30):
        ray_end_position = sd.get_point(
            ray_start_position.x + ray_length * sd.sin(angle),
            ray_start_position.y + ray_length * sd.cos(angle)
        )
        sd.line(ray_start_position, ray_end_position, width=3, color=sd.COLOR_YELLOW)

draw_sun()
