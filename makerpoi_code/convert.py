#   Convert Images To Poi Program
#   Chris Butulis 
#   Last Updated: 5.21.19
#   Python Version: 3.7.2

#**IMPORTANT NOTES: THIS FILE CONVERTS convert.jpg to makerpoi_code.ino**#
#Proper syntax is in shell as follows: $python convert.py convert.jpg > makerpoi_code.ino

#IMPORTS
import cv2
import numpy as np
from PIL import Image
import os

#DEFINITIONS 
pixels = 32 #Number of pixels in use in Poi
custom_delay = 1 #Add a custom delay if the image appears stretched 

#GET THE IMAGE
img = Image.open('convert.jpg')
h,w,d = np.shape(img)

#RESIZE IMAGE TO FIT POI 
new_height = pixels
new_width = new_height * w // h
img = img.resize((new_width, new_height), Image.ANTIALIAS)
img = img.convert('RGB')
img.save('convert.jpg')
h,w,d = np.shape(img)

#PREPARE ARRAY
arr = np.asarray(img)
arr = arr[:, :, :3]  
size = len(arr) 

#PUT PIXEL VALUES IN ARRAY
with open('temp.txt', 'a') as f:
    for i in range (w): 
        for j in range(len(arr)): 
            if j > pixels:
                break;
            print("strip.setPixelColor(",(j), "",  arr[j, i], ");", end="\n", file=f)
        print("strip.show();", end="\n", file=f)
        print("delay("+custom_delay+");", end="\n", file=f)
            
#REMOVE BRACKETS
with open("temp.txt", "rt") as fin: 
    with open("temp1.txt", "wt") as fout:
        for line in fin:
            fout.write(line.replace(' [', ''))

#REMOVE BRACKETS
with open("temp1.txt", "rt") as fin: 
    with open("temp2.txt", "wt") as fout:
        for line in fin:
            fout.write(line.replace('] ', ''))

#ADD COMMAS
with open("temp2.txt", "rt") as fin: 
    with open("temp3.txt", "wt") as fout:
        for line in fin:
            fout.write(line.replace(' ', ', '))

#REMVOE EXTRA COMMAS
with open("temp3.txt", "rt") as fin: 
    with open("temp4.txt", "wt") as fout: 
        for line in fin:
            fout.write(line.replace('(, ', '('))

#REMOVE EXTRA COMMAS
with open("temp4.txt", "rt") as fin: 
    with open("temp5.txt", "wt") as fout: 
        for line in fin:
            fout.write(line.replace(', , , ', ', '))

#REMOVE EXTRA COMMAS
with open("temp5.txt", "rt") as fin: 
    with open("temp6.txt", "wt") as fout: 
        for line in fin:
            fout.write(line.replace(', , ', ', '))

#PUT THE BASE CODE AT THE TOP                
with open("temp6.txt", "rt") as fin: 
    with open("output.txt", "wt") as fout: 
        fout.write("#define VBATPIN 2\n#include <Adafruit_NeoPixel.h>\n#define PIN 1\n#define NUM_LEDS 32\nAdafruit_NeoPixel strip = Adafruit_NeoPixel(32, PIN, NEO_GRB + NEO_KHZ800);\nfloat measuredvbat;\nvoid setup() {\nstrip.begin();\nstrip.setBrightness(40);\nmeasuredvbat = bat();\nfor(int i=0; i<32; i++) {\nif(measuredvbat > 3.5)\nstrip.setPixelColor(i, 0, 255, 0);\nif(measuredvbat > 3.29 && measuredvbat < 3.31)\nstrip.setPixelColor(i, 0, 0, 255);\nif(measuredvbat < 3.29)\nstrip.setPixelColor(i, 255, 0, 0);\n}\nstrip.show();\ndelay(500);\nstrip.clear();\nstrip.show();\n}\nfloat bat() {\nfloat measuredvbat = analogRead(VBATPIN);\nreturn measuredvbat*3.30/1023;\n}\nvoid loop() {\nwhile(measuredvbat > 3.29) {\ndelay(1);\n}\n")
        fout.write(fin.read())
        fout.write("}")

#WRITE OUTPUT TO FINAL FILE
f = open('output.txt')
file_contents = f.read()
print(file_contents)

#REMOVE REVISION FILES
os.remove('temp.txt')
os.remove('temp1.txt')
os.remove('temp2.txt')
os.remove('temp3.txt')
os.remove('temp4.txt')
os.remove('temp5.txt')         
os.remove('temp6.txt')

    
