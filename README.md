# LED-project
This is a project that can convert relatively small images for use on POI with arduino based operating systems. Additionally, it contains the documentation necessescary to create POI with your own materials, and the difficulties I found along the way. The project is currently in development. While most of the base software has been completed, many features have not been completed yet. 

# Running and Compiling the Program:

First begin by placing the desired image, titled convert.jpg into the program directory

Then, execute the run.bat file in the program directory

Examine the arduino code file, and ensure that are variables are set correctly 

  -Make sure the Pinout is correct
  
  -Make sure the numleds is correct
  
# The Stages of Development
The project is based off of python 3.7 and C++ (Which is used by arduino IDE). The link to python 3.7 is (https://www.python.org/downloads/release/python-373/) and the link to arduino IDE is (https://www.arduino.cc/en/main/software). For the python install, remember to set environment variables. In addition to python, one must also install/upgrade pip, which can be done from the command line using: 

py -m pip upgrade pip

Then, install all libraries requisite for the convert image program (cv2, PIL, and numpy). However PIL has been deprecated, and PILLOW is in use with more recent versions of python. To install it, use:

 py -m pip install pillow
 
This should meet all of the basic installation requirements for the project. However, there are some aspects of the ardino IDE that may need to be tweaked. The SAMD boards for arduino have to be installed, in addition to the Neopixel library. With this, all of the software should be configured.

 # Hardware: 
The project requires a host of hardware. All of which can be purchased from Adafruit's website or Amazon. For the project, I used the following parts: 

ALITOVE 3.2ft 144 Pixels WS2812B Individually Addressable LED Strip Light (https://www.amazon.com/gp/product/B019DYZNO6/ref=ppx_yo_dt_b_asin_title_o07_s00?ie=UTF8&psc=1)

2 of Adafruit Trinket M0 - for use with CircuitPython & Arduino IDE (https://www.amazon.com/gp/product/B01MR2S7K0/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1)

Breadboard and generic wires (Avaliable from numerous electronic stores)

Micro-USB cable (https://www.amazon.com/AmazonBasics-Male-Micro-Cable-Black/dp/B072J1BSV6/ref=sxin_0?keywords=micro+usb+cable&pd_rd_i=B072J1BSV6&pd_rd_r=1f60e8bf-2f5e-42c2-9791-e50e9b2abf8a&pd_rd_w=FoFq3&pd_rd_wg=MO36n&pf_rd_p=0395a9fd-d124-46c0-a48f-d8582ed1a45c&pf_rd_r=XZNYJEVAKXEE38TJZNQV&qid=1554648616&s=electronics)

2 of uxcell Power Supply DC 3.7V 500mAh Li-po batteries (https://www.amazon.com/gp/product/B0767D8GVG/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1)

2 of Adafruit LiIon/LiPoly Backpack Add-On for Pro Trinket/ItsyBitsy (https://www.adafruit.com/product/2124)

In total, the project cost me around $66.00, as I had a breadboard, wires, and cables. 

# Assembly

The initial development board appeared as so, with some soldering required for the test board:

# Software Development

The software development began with the convert.py script developed in python. It converts the image to an rgb array, and prints it out in the format of a header file. This process was not easy, and the file was cleaned by multiple replace functions. It can be run with the run.bat file. 

Then, the project progressed to writing the arduino code. 
