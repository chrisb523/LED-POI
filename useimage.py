import numpy as np

rgb_values = open('output.txt', 'r')

rgbArray = rgb_values.read().split('\n')

size = len(rgbArray)

for i in range(0,size):
    i = i+1
    print(rgbArray[i])
    print()
