from sense_hat import SenseHat

sense=SenseHat()


green=(0,255,0)
white=(255,255,255)
red=(255,0,0)


while True:
    humidity=sense.humidity
    humidity_value=64*humidity/100
    print(humidity)


    pixels=[red if i < humidity_value else white for i in range(64)]
    sense.set_pixels(pixels)