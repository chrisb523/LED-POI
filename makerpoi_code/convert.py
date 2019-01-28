#Convert Images To Array
#   Chris Butulis 
#   Last Updated: 1.25.19
#   Python Version: 3.7.2

#**IMPORTANT NOTES: THIS FILE CONVERTS convert.jpg to output.txt**#
import cv2
import numpy as np
from PIL import Image
import os

pixels = 32 #Number of pixels in use in Poi

img = Image.open('convert.jpg')
h,w,d = np.shape(img)

arr = np.asarray(img)
arr = arr[:, :, :3] #Cuts off extraneous channels 
size = len(arr) #add 1 due to the first init line
j=0 #counter variable

with open('temp.txt', 'a') as f:

    print("const uint8_t PROGMEM values[][3] = {", file=f)
    for i in range (len(arr)):
        for j in range(1, h): #Specifiy a second condition for image length
            if j > pixels:
                break;
            j=j+1
            print("{", end="", file=f) 
            print(arr[i,j], end="", file=f)
            if j == pixels+1:
                print("}", end="", file=f)
            else:
                print("},", end="", file=f)
            print("\n", end="", file=f)
    print("};", file=f)

with open("temp.txt", "rt") as fin: #Remove brackets
    with open("temp1.txt", "wt") as fout:
        for line in fin:
            fout.write(line.replace('[', ''))

with open("temp1.txt", "rt") as fin:
    with open("temp2.txt", "wt") as fout:
        for line in fin:
            fout.write(line.replace(']', ''))

with open("temp2.txt", "rt") as fin: #remove double spaces
    with open("temp3.txt", "wt") as fout:
        for line in fin:
            fout.write(line.replace('  ', ' '))

with open("temp3.txt", "rt") as fin: #Add commas
    i=0 #counter variable
    with open("output.txt", "wt") as fout:
        for line in fin:
            i+=1
            if i == 1:
                fout.write(line)
            else:
               fout.write(line.replace(' ', ', '))
        
f = open('output.txt')
file_contents = f.read()
print(file_contents)

os.remove("temp.txt")
os.remove("temp1.txt")
os.remove("temp2.txt")
os.remove("temp3.txt")

            


    
