#   Convert Images To Array
#   Chris Butulis 
#   Last Updated: 4.7.19
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

with open('temp.txt', 'a') as f:
    print("uint8_t values[][3] = {", file=f)
    for i in range (w): #could also use len(arr)?
        for j in range(len(arr)): #Specifiy a second condition for image length
            if j > pixels:
                break;
            print("{", end="", file=f) 
            print(arr[j, i], end="", file=f)
            print("},", end="", file=f)
            print("\n", end="", file=f)
    print("};", file=f)

with open("temp.txt", "rt") as fin: #Remove brackets
    with open("temp1.txt", "wt") as fout:
        i=0
        for line in fin:
            i+=1
            if i == 1:
                fout.write(line)
            else:
                fout.write(line.replace('[', ''))

with open("temp1.txt", "rt") as fin: #remove brackets
    with open("temp2.txt", "wt") as fout:
        i=0 
        for line in fin:
            i+=1
            if i == 1:
                fout.write(line)
            else:
                fout.write(line.replace(']', ''))

with open("temp2.txt", "rt") as fin: #remove double spaces
    with open("temp3.txt", "wt") as fout:
        for line in fin:
            fout.write(line.replace('  ', ' '))

with open("temp3.txt", "rt") as fin: #Add commas
    i=0 #counter variable
    with open("temp4.txt", "wt") as fout:
        for line in fin:
            i+=1
            if i == 1:
                fout.write(line)
            else:
               fout.write(line.replace(' ', ', '))

with open("temp4.txt", "rt") as fin: #Remove brackets
    with open("temp5.txt", "wt") as fout:
        i=0
        for line in fin:
            i+=1
            if i == 1:
                fout.write(line)
            else:
                fout.write(line.replace('{, ', '{'))               

with open("temp5.txt", "rt") as fin: #Remove brackets
    with open("temp6.txt", "wt") as fout:
        i=0
        for line in fin:
            i+=1
            if i == 1:
                fout.write(line)
            else:
                fout.write(line.replace(', , ', ', '))   

with open("temp6.txt", "rt") as fin: #Remove last comma
    with open("output.txt", "wt") as fout:
        compare = 0 #Counter variable to compare current iteration to required one
        for line in fin:
            compare+=1
            if compare == (i-1):
                fout.write(line.replace('},', '}'))
            else:
                fout.write(line)
        
f = open('output.txt')
file_contents = f.read()
print(file_contents)

os.remove("temp.txt")
os.remove("temp1.txt")
os.remove("temp2.txt")
os.remove("temp3.txt")
os.remove("temp4.txt")
os.remove("temp5.txt")
os.remove("temp6.txt")            


    
