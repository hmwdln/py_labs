import simple_draw as sd
sd.resolution = (1600, 900)

def floor():
    sd.rectangle(sd.Point(0, 0), sd.Point(1600, 100), color = sd.COLOR_DARK_ORANGE, width = 0) 
    
floor()