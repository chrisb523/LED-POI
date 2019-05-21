#   Convert Images To Poi Program
#   Chris Butulis 
#   Last Updated: 5.10.19
#   Python Version: 3.7.2

#**IMPORTANT NOTES: THIS FILE CONVERTS convert.jpg to makerpoi_code.ino**#
#Proper syntax is in shell as follows: $python convert.py convert.jpg > makerpoi_code.ino

import cv2
import numpy as np
from PIL import Image
import os

pixels = 32 #Number of pixels in use in Poi

img = Image.open('convert.jpg')
h,w,d = np.shape(img)

new_height = 32
new_width = new_height * w // h
img = img.resize((new_width, new_height), Image.ANTIALIAS)
img = img.convert('RGB')
img.save('convert.jpg')
h,w,d = np.shape(img)

arr = np.asarray(img)
arr = arr[:, :, :3] #Cuts off extraneous channels 
size = len(arr) #add 1 due to the first init line

with open('temp.txt', 'a') as f:
    for i in range (w): 
        for j in range(len(arr)): #Specifiy a second condition for image length
            if j > pixels:
                break;
            print("strip.setPixelColor(",(j), "",  arr[j, i], ");", end="\n", file=f)
        print("strip.show();", end="\n", file=f)
        print("delay(1);", end="\n", file=f)
            

with open("temp.txt", "rt") as fin: #remove double spaces
    with open("temp1.txt", "wt") as fout:
        for line in fin:
            fout.write(line.replace(' [', ''))

with open("temp1.txt", "rt") as fin: #remove double spaces
    with open("temp2.txt", "wt") as fout:
        for line in fin:
            fout.write(line.replace('] ', ''))

with open("temp2.txt", "rt") as fin: #remove double spaces
    with open("temp3.txt", "wt") as fout:
        for line in fin:
            fout.write(line.replace(' ', ', '))

with open("temp3.txt", "rt") as fin: 
    with open("temp4.txt", "wt") as fout: 
        for line in fin:
            fout.write(line.replace('(, ', '('))

with open("temp4.txt", "rt") as fin: 
    with open("temp5.txt", "wt") as fout: 
        for line in fin:
            fout.write(line.replace(', , , ', ', '))

with open("temp5.txt", "rt") as fin: 
    with open("temp6.txt", "wt") as fout: 
        for line in fin:
            fout.write(line.replace(', , ', ', '))
                   
with open("temp6.txt", "rt") as fin: 
    with open("output.txt", "wt") as fout: 
        fout.write("#include <Adafruit_NeoPixel.h>\n#define PIN 1\n#define NUM_LEDS 32\nAdafruit_NeoPixel strip = Adafruit_NeoPixel(32, PIN, NEO_GRB + NEO_KHZ800);\nvoid setup() {\nstrip.begin();\nstrip.setBrightness(40);\n}\nvoid loop() {\n")
        fout.write(fin.read())
        fout.write("}")

f = open('output.txt')
file_contents = f.read()
print(file_contents)

os.remove('temp.txt')
os.remove('temp1.txt')
os.remove('temp2.txt')
os.remove('temp3.txt')
os.remove('temp4.txt')
os.remove('temp5.txt')         
os.remove('temp6.txt')

    
