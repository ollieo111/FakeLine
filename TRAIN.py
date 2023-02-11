from PIL import Image, ImageDraw, ImageFont
import time

print("welcome to fakeline made by oxz#5150!")
time.sleep(5)
start = input("where are you traviling to example KGX: ")
print("")
arrive = input("where are you traviling from ex NCL: ")
print("")
place1 = input("enter the full name of the place your going to ex LONDON KINGS CROSS: ")
print("")
place2 = input("enter the full name of the place your going from ex NEWCASTLE UPON TYNE: ")
print("")
code = input("please enter a random 11 digit code ALL CAPITALS no numbers: ")
print("")
date = input ("please enter the date your going in this format 06 Sep 2023: ")
print("")
depart = input("enter the time your train is departing ex 20:41: ")


image = Image.open("123I.jpg")


draw = ImageDraw.Draw(image)

font1 = ImageFont.truetype("arial.ttf", 70)
font2 = ImageFont.truetype("arial.ttf", 20)
font3 = ImageFont.truetype("arial.ttf", 30)
font4 = ImageFont.truetype("arial.ttf", 45)

x = 28
y = 169

draw.text((x, y), start, font=font1, fill=(0, 0, 0))


x = 507
y = 169


draw.text((x, y), arrive, font=font1, fill=(0, 0, 0))

print("choosing colors")

x = 400
y = 130


draw.text((x, y), place1, font=font2, fill=(114, 114, 114))


x = 28
y = 130

draw.text((x, y), place2, font=font2, fill=(114, 114, 114))

print("writing your destination")

x = 210
y = 408


draw.text((x, y), depart, font=font3, fill=(0, 0, 0))

x = 240
y = 929


draw.text((x, y), code, font=font3, fill=(0, 0, 0))

print("5 seconds!")

x = 100
y = 32

draw.text((x, y), date, font=font4, fill=(0, 0, 0))

time.sleep(3)

image.save("Trainline.jpg")

print("DONE please check for Trainline dot jpg in the folder that this program is in")