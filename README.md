# Software from this rep Not supported more. Actual scripts will be [here](https://github.com/pieeg-club/PiEEG) , now just only Python. It is a old version with C language.    


# To Buy - PiEEG is available in the market at our partner shop [Elecrow](https://pieeg.com/pieeg/)

This project is the result of several years of work on the development of BCI. We believe that the easiest way to get started with biosignals is to use a shield.
We will try to reveal the process of reading EEG signals as fully and clearly as possible. 



[![Tweet](https://img.shields.io/twitter/url/http/shields.io.svg?style=social)](https://twitter.com/intent/tweet?text=DIY%20Brain-Computer%20Interface%20PIEEG%20&url=https://github.com/Ildaron/EEGwithRaspberryPI&hashtags=RaspberryPI,EEG,python,opensource)

![alt tag](https://github.com/Ildaron/EEGwithRaspberryPI/blob/master/Supplementary%20files/fig.15...jpg "general view")​
-  [Warning](https://github.com/Ildaron/EEGwithRaspberryPI#warning)
-  [How it Works](https://github.com/Ildaron/EEGwithRaspberryPI/blob/master/README.md#how-it-works)
-  [Noise Measure](https://github.com/Ildaron/EEGwithRaspberryPI#noise-measure)
-  [Device Pinout](https://github.com/Ildaron/EEGwithRaspberryPI/blob/master/README.md#device-pinout)   
-  [Description of Code](https://github.com/Ildaron/EEGwithRaspberryPI/blob/master/README.md#description-of-code)
-  [Video-Hardware and Signal Processing Demonstration](https://github.com/Ildaron/EEGwithRaspberryPI/blob/master/README.md#video---hardware-and-signal-processing-demonstration) 
-  [For Beginners](https://github.com/Ildaron/EEGwithRaspberryPI/blob/master/README.md#for-beginners)        
-  [Citation](https://github.com/Ildaron/EEGwithRaspberryPI/blob/master/README.md#citation)   
-  [Contacts](https://github.com/Ildaron/EEGwithRaspberryPI#contacts)  

#### How it Works   
 [1.1.Read_data.c](https://github.com/Ildaron/EEGwithRaspberryPI/blob/master/1.1.Read_data.c) C script for reading data in real-time and saving to a txt file  
 [1.2.Read_data.cpp](https://github.com/Ildaron/EEGwithRaspberryPI/blob/master/1.2.Read_data.cpp) C++ script for reading data in real-time and saving to a txt file   
 [real_time.py](https://github.com/Ildaron/EEGwithRaspberryPI/blob/master/GUI/real_time.py) GUI python script for reading data in real-time    
 [robot_control.py](https://github.com/Ildaron/EEGwithRaspberryPI/blob/master/Robot_control/robot_control.py) script to control a robot by blinking  

Connect the shield to Raspberry Pi 3 or Raspberry Pi 4 and after that connect the device to a battery (power supply) and connect electrodes.
Full galvanic isolation from mains required.  
This also applies to the monitor. Use only a monitor that is powered by the Raspberry Pi, as in the picture below, left. Electrodes positioned according to the International 10-20 system, right.    
![alt tag](https://github.com/Ildaron/EEGwithRaspberryPI/blob/master/Supplementary%20files/fig.7.bmp "general view")​

#### Device Pinout  
Shield connected with Raspberry Pi only at the next points:     
  43  +5V  
  44  GND  
  37  MOSI  
  34  MISO  
  35  CLK  
  36  CS  

  
#### Description of Code  
Python script does not allow reading data from ADS1299 with a frequency of 250 Hz. It's necessary to use .c or .cpp scripts for reading data in real-time and Python for signal processing and visualization.   


#### Video - Control Robot Toy by Blinking  
[![Software demonstrations](https://github.com/Ildaron/EEGwithRaspberryPI/blob/master/Supplementary%20files/fig.18.jpg)](https://youtu.be/wNgCEKIXGUY)      

#### Citation  
I. Rakhmatuiln, M. Zhanikeev, and A. Parfenov, "Raspberry Pi Shield - for measure EEG (PIEEG)," 2021 5th International Conference on Electrical, Electronics, Communication, Computer Technologies and Optimization Techniques (ICEECCOT), 2021, pp. 410-413, DOI: 10.1109/ICEECCOT52851.2021.9707969  [link](https://ieeexplore.ieee.org/document/9707969)

Rakhmatulin, I., Volkl, S. (2020). PIEEG: Turn a Raspberry Pi into a Brain-Computer Interface to measure biosignals. arXiv:2201.02228, https://arxiv.org/abs/2201.02228  

#### Contacts  
http://pieeg.com/


#### Warnings
>[!WARNING]
> You are fully responsible for your personal decision to purchase this device and, ultimately, for its safe use. PiEEG is not a medical device and has not been certified by any government regulatory agency for use with the human body. Use it at your own risk.  

>[!CAUTION]
> The device must operate only from a battery - 5 V. Complete isolation from the mains power is required.! The device MUST not be connected to any kind of mains power, via USB or otherwise.   
> Power supply - only battery 5V, please read the datasheet!!!!!  
