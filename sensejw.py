from sense_hat import SenseHat
import random

sense=SenseHat()



green=[255,255,0]
blue=[0,0,255]
red=[255,0,0]
black=[0,0,0]
"""
rcol1=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]
rcol2=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]
sense.show_message("BEANS",scroll_speed=0.05,text_colour=rcol1,back_colour=rcol2)
rcol2=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]
rcol1=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]
sense.show_message("IS"   ,scroll_speed=0.05,text_colour=rcol1,back_colour=rcol2)
rcol2=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]
rcol1=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]
sense.show_message("THE " ,scroll_speed=0.05,text_colour=rcol1,back_colour=rcol2)
rcol2=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]
rcol1=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]
sense.show_message("BEST" ,scroll_speed=0.05,text_colour=rcol1,back_colour=rcol2)
rcol2=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]
rcol1=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]
sense.show_message("HORSE",scroll_speed=0.05,text_colour=rcol1,back_colour=rcol2)
rcol2=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]
rcol1=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]
sense.show_message("IN"   ,scroll_speed=0.05,text_colour=rcol1,back_colour=rcol2)
rcol2=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]
rcol1=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]
sense.show_message("THE"  ,scroll_speed=0.05,text_colour=rcol1,back_colour=rcol2)
rcol2=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]
rcol1=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]
sense.show_message("WORLD",scroll_speed=0.05,text_colour=rcol1,back_colour=rcol2)
"""

sense.clear()

def jwprint(mytext):
   
	rcol1=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]
	rcol2=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]
	sense.show_message(mytext,scroll_speed=0.05,text_colour=rcol1,back_colour=rcol2)
	return

"""
jwprint("Hello")
jwprint("dad")
jwprint("your")
jwprint("very")
jwprint("clever")
sense.clear()
"""
i=0
while i<10:
	temp=sense.get_temperature()


	temp=round(temp,1)
	jwprint(str(temp))
	i=i+1
sense.clear()

