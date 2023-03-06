import simple_draw as sd

sd.resolution = (1600, 900)

def smile():
    s = sd.get_point(1120, 150)
    point_list = [sd.Point(s.x - 15, s.y - 5), sd.Point(s.x - 8, s.y - 10), sd.Point(s.x + 8, s.y - 10), sd.Point(s.x + 15, s.y - 5)]

    sd.circle(center_position = s, radius = 50)
    sd.circle(center_position = sd.Point(s.x - 20, s.y + 20), radius = 12)
    sd.circle(center_position = sd.Point(s.x + 20, s.y + 20), radius = 12)

    sd.lines(point_list)

    sd.line(sd.get_point(1120, 100), sd.get_point(1120, 50)) # туловище
    sd.line(sd.get_point(1120, 85), sd.get_point(1100, 65)) # левая рука
    sd.line(sd.get_point(1120, 85), sd.get_point(1140, 65)) # правая рука
    sd.line(sd.get_point(1120, 50), sd.get_point(1100, 25)) # левая нога
    sd.line(sd.get_point(1120, 50), sd.get_point(1140, 25)) # правая нога

smile()
