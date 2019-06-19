#   Convert Images To Pixel Array
#   Chris Butulis 
#   Last Updated: 6.6.19
#   Python Version: 3.7.2

#IMPORTANT NOTES: This Program Converts jpg file(s) into makerpoi_code.ino
#Proper syntax is in shell as follows: $python convert.py

#IMPORTS
import cv2
import numpy as np
from PIL import Image
import os
import glob

#DEFINITIONS 
pixels = 32 #Number of pixels in use in Poi

#GET DIRECTORY
dx = glob.glob('*.jpg')
numimg = len(dx)

#PLACE RGB VALUES IN FILE
for x in range (0, len(dx)):
    #RESIZE IMAGES TO CORRECT VALUES DEPENDING ON POI SIZE
    name = dx[x]
    img = Image.open(name)
    h,w,d = np.shape(img)
    new_height = pixels
    new_width = new_height * w // h
    img = img.resize((new_width, new_height), Image.ANTIALIAS)
    img = img.convert('RGB')
    img.save(name)
    #Prepare ARRAY
    arr = np.asarray(img)
    arr = arr[:, :, :3]  
    size = len(arr)
    h,w,d = np.shape(img)
    #PUT PIXEL VALUES IN ARRAY
    with open('temp.txt', 'a') as f:
        print('void image{}()'.format(x), '{', end="\n", file=f)
        for i in range (w): 
            for j in range(size): 
                if j > pixels:
                    break;
                print("strip.setPixelColor(",(j), "",  arr[j, i], ");", end="\n", file=f)
            print("strip.show();", end="\n", file=f)
            print("delay(1);", end="\n", file=f)
        print('}', end="\n", file=f)

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

#REMOVE COMMAS IN VOID STATEMNTS 
with open("temp6.txt", "rt") as fin: 
    with open("temp7.txt", "wt") as fout: 
        for line in fin:
            fout.write(line.replace('void, ', 'void '))

#REMOVE COMMAS IN VOID STATEMNTS 
with open("temp7.txt", "rt") as fin: 
    with open("temp8.txt", "wt") as fout: 
        for line in fin:
            fout.write(line.replace('(),', '()'))

#PUT THE BASE CODE AT THE TOP                
with open("temp8.txt", "rt") as fin: 
    with open("output.txt", "wt") as fout: 
        fout.write('#define VBATPIN 2\n#include <Adafruit_NeoPixel.h>\n#define PIN 1\n#define NUM_LEDS 32\n#define Button 3\nAdafruit_NeoPixel strip = Adafruit_NeoPixel(32, PIN, NEO_GRB + NEO_KHZ800);\nfloat measuredvbat;\nint buttonState = 0;\nint img = 1;\n' + 'int numimg={}'.format(numimg) + ';\nvoid setup() {\nstrip.begin();\nstrip.setBrightness(40);\nmeasuredvbat = bat();\nfor(int i=0; i<32; i++) {\nif(measuredvbat > 1.5 && measuredvbat < 2)\nstrip.setPixelColor(i, 0, 255, 0);\nif(measuredvbat > 3.29 && measuredvbat < 3.31)\nstrip.setPixelColor(i, 0, 0, 255);\nif(measuredvbat < 1.5)\nstrip.setPixelColor(i, 255, 0, 0);\n}\nstrip.show();\ndelay(500);\nstrip.clear();\nstrip.show();\npinMode(Button, INPUT);\n}\nfloat bat() {\nfloat measuredvbat = analogRead(VBATPIN);\nreturn measuredvbat*3.30/1023;\n}\nvoid loop() {\nwhile(measuredvbat > 3.29) {\ndelay(1);\n}\nbuttonState = digitalRead(Button);\nif (buttonState == HIGH) {\nimg++;\ndelay(32);\n}\nif(img > numimg)\nimg = 1;\n\n')
        for i in range (len(dx)):
            fout.write('if(img=={})\n'.format(i+1))
            fout.write('image{}();\n'.format(i))
        fout.write("}\n")
        fout.write(fin.read())


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
os.remove('temp7.txt')
os.remove('temp8.txt')
    
