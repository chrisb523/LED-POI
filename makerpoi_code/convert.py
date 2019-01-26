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
size = len(arr)
i=0

with open('temp.txt', 'a') as f:
    for i in range (1,10):
        i=i+1
        for i in range (1, h): #Specifiy a second condition for image length
            print(arr[i,i], file=f)

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
    with open("output.txt", "wt") as fout:
        for line in fin:
            fout.write(line.replace(' ', ', '))

f = open('output.txt')
file_contents = f.read()
print(file_contents)

os.remove("temp.txt")
os.remove("temp1.txt")
os.remove("temp2.txt")
os.remove("temp3.txt")

            


    
