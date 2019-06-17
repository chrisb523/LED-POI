# LED POI Project
This is a project that can convert images for use on POI with arduino based operating systems. Additionally, it contains the documentation necessescary to create your own POI with materials listed below. Furthermore, it lists some of the difficulties I found along the way developing both the software and hardware components, and the solutions I found to solve them. The project is still in development, but most features are reliable and tested. Feel free to modify the code or project hardware as you wish, or even add your own features.  

# Running and Compiling the Program:

First begin by placing the desired image, which must be in the JPEG format (.jpg) into the arduino program directory (/makerpoi_code/)

Then, ensure that the number of pixels is correctly defined in convert.py (only nessescary if you change the number of LEDs)
Before running the program, see the software section, and ensure you have all of the dependencies

Execute the run.bat file in the program directory, or use a shell to execute the convert.py program

Examine the arduino code file, and ensure that are variables are set correctly to the specifications of the project 
  -Make sure the Pinout is correct
  -Make sure the voltages in the battery measuring function are correct (depending on whether you are using 3.3v or 5v logic)
  
# Software: 
The project is based off of python 3.7 and C++ (Which is used by arduino IDE). The link to python 3.7 is (https://www.python.org/downloads/release/python-373/) and the link to arduino IDE is (https://www.arduino.cc/en/main/software). For the python install, remember to set environment variables. In addition to python, one must also install/upgrade pip, which can be done from the command line using: 

py -m pip upgrade pip

Then, install all libraries requisite for the convert image program (cv2, PIL, and numpy). However PIL has been deprecated, and PILLOW is in use with more recent versions of python. To install it, use:

 py -m pip install pillow
 
This should meet all of the basic installation requirements for the project. However, there are some aspects of the ardino IDE that may need to be tweaked. The SAMD boards for arduino have to be installed, in addition to the Neopixel library. With this, all of the software should be configured correctly.

Also, install the Trinket m0 board using this link: https://adafruit.github.io/arduino-board-index/package_adafruit_index.json

 # Hardware: 
The project requires a host of hardware. All of the hardware can be purchased from Adafruit's website or Amazon. For the project, I used the following parts: 

ALITOVE 3.2ft 144 Pixels WS2812B Individually Addressable LED Strip Light (https://www.amazon.com/gp/product/B019DYZNO6/ref=ppx_yo_dt_b_asin_title_o07_s00?ie=UTF8&psc=1)

2 of Adafruit Trinket M0 - for use with CircuitPython & Arduino IDE (https://www.amazon.com/gp/product/B01MR2S7K0/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1)

Breadboard and generic wires (Avaliable from numerous electronic stores)

Micro-USB cable (https://www.amazon.com/AmazonBasics-Male-Micro-Cable-Black/dp/B072J1BSV6/ref=sxin_0?keywords=micro+usb+cable&pd_rd_i=B072J1BSV6&pd_rd_r=1f60e8bf-2f5e-42c2-9791-e50e9b2abf8a&pd_rd_w=FoFq3&pd_rd_wg=MO36n&pf_rd_p=0395a9fd-d124-46c0-a48f-d8582ed1a45c&pf_rd_r=XZNYJEVAKXEE38TJZNQV&qid=1554648616&s=electronics)

2 of uxcell Power Supply DC 3.7V 500mAh Li-po batteries (https://www.amazon.com/gp/product/B0767D8GVG/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1)

2 of Adafruit LiIon/LiPoly Backpack Add-On for Pro Trinket/ItsyBitsy (https://www.adafruit.com/product/2124)

Any Nylon Rope

In total, the project cost me around $66.00, as I had a breadboard, wires, nylon cord, and cables. 
-------------------------------------------------------------------------------------------------------
Additional Items:
If you so wish to build the cases for the POI, it will cost extra, but I found that it was important to build them to protect from water damage and collisions. 

4 Vinyl Caps
(https://www.amazon.com/gp/product/B0747RVMRZ/ref=ppx_yo_dt_b_asin_title_o04_s00?ie=UTF8&psc=1)

Clear Polycarbonate Tubing, 1-1/8" ID, 1-1/4" OD, 1/16" Wall, 3' Length
(https://www.amazon.com/gp/product/B000OMFLD0/ref=ppx_yo_dt_b_asin_title_o05_s00?ie=UTF8&psc=1)

Tissue Paper or Towels - To act as a shock absorber and spacer

# Assembly

The initial development board appeared as so, with some soldering required for the test board:

# Software Development

The software development began with the convert.py script developed in python. It converts the image to an rgb array, and prints it out in the format of a header file. This process was not easy, and the file was cleaned by multiple replace functions. It can be run with the run.bat file. 

Initially, I had written the python script to export a header file that contained all of the rgb values in arrays. However, I later decided to make the python script handle the placements of these values directly into the files. This reduced the time taken by the trinket board to process the images, and allowed for a clearer image with higher resolution. 

With the second version of the project, I added a battery detector to tell the user whether or not the battery is running low, using the colors red and green. This was enabled by the soldering of the usb pin to an analog read pin, and a software analog read function that detetected the voltage on startup. Futhermore, this feature also has the ability to prevent the POI from displaying the image at all if the POI are charging or plugged into a computer for code upload. Instead, the POI will flash blue one time. This works due to the property that the USB pin outputs differing voltages based on factors such as battery level, and whether or not the POI are charging. 
