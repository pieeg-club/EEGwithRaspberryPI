# The easiest way to the neuroscience world with the shield for RaspberryPi - [PIEEG](https://www.hackerbci.com/). Real-Time signal processing GUI in python.  Open-source. 
This project is the result of several years of work on the development of BCI. We believe that the easiest way to get started with biosignals is to use a shield.
We will try to reveal the process of reading EEG signals as fully and clearly as possible. 

[![Tweet](https://img.shields.io/twitter/url/http/shields.io.svg?style=social)](https://twitter.com/intent/tweet?text=DIY%20Brain-Computer%20%20interface%20PIEEG%20&url=https://github.com/Ildaron/EEGwithRaspberryPI&hashtags=RaspberryPI,EEG,python,opensource)

![alt tag](https://github.com/Ildaron/EEGwithRaspberryPI/blob/master/Supplementary%20files/Fig.3.jpg "general view")​

-  [How it Works](https://github.com/Ildaron/EEGwithRaspberryPI/blob/master/README.md#how-it-works)
-  [Noise measure](https://github.com/Ildaron/EEGwithRaspberryPI#noise-measure)
-  [Device pinout](https://github.com/Ildaron/EEGwithRaspberryPI/blob/master/README.md#device-pinout)   
-  [Description of code](https://github.com/Ildaron/EEGwithRaspberryPI/blob/master/README.md#description-of-code)
-  [Video-hardware and signal processing demonstration](https://github.com/Ildaron/EEGwithRaspberryPI/blob/master/README.md#video---hardware-and-signal-processing-demonstration) 
-  [For beginners](https://github.com/Ildaron/EEGwithRaspberryPI/blob/master/README.md#for-beginners)        
-  [Citation](https://github.com/Ildaron/EEGwithRaspberryPI/blob/master/README.md#citation)   
-  [Contacts](https://github.com/Ildaron/ironbci/blob/master/README.md#8-contacts)  

#### How it Works   
Connect the shield to Raspberry PI 3 or RaspberryPI4 and after that connect the device to a battery (power supply) and connect electrodes.
Full galvanic isolation from mains required.  
This also applies to the monitor. Use only a monitor that is powered by the RaspberryPI, as in the picture below, left. Electrodes positioned according to International 10-20 system, right.    
![alt tag](https://github.com/Ildaron/EEGwithRaspberryPI/blob/master/Supplementary%20files/fig.7.bmp "general view")​

#### Device pinout  
Shiled connceted with raspbberryPI only in the netxt points     
  43  +5V  
  44  GND  
  37  MOSI  
  34  MISO  
  35  CLKL  
  36  CS  
  
#### Noise measure


Chewing artifact (4-3-2-1), in real-time for 8 electrodes via [real_time.py](https://github.com/Ildaron/EEGwithRaspberryPI/blob/master/GUI/real_time.py) 
![alt tag](https://github.com/Ildaron/EEGwithRaspberryPI/blob/master/Supplementary%20files/fig.14.jpg "general view")​  

Blinking artifact, after Chewing. [Raw data](https://github.com/Ildaron/EEGwithRaspberryPI/blob/master/dataset/2.Blinking_Chewing.txt)
![alt tag](https://github.com/Ildaron/EEGwithRaspberryPI/blob/master/Supplementary%20files/fig.9.row_dara.bmp "general view")​  
[Raw data](https://github.com/Ildaron/EEGwithRaspberryPI/blob/master/dataset/2.Blinking_Chewing.txt) with [band-pass filter](https://github.com/Ildaron/EEGwithRaspberryPI/blob/master/2.Data_filter.py) (1-40Hz)
![alt tag](https://github.com/Ildaron/EEGwithRaspberryPI/blob/master/Supplementary%20files/fig.10.band_bass.bmp "general view")​  
Alpha wave detection eyes open, eyes closed  
![alt tag](https://github.com/Ildaron/EEGwithRaspberryPI/blob/master/Supplementary%20files/Fig.11.alpha.bmp "general view")​  
#### Description of the code  
Python script dont allow reading data from ADS1299 with the frequency of 250 Hz. Necessary to use .c or .cpp scripts for reading data in real-time and python for signal processing and vialuzation.   
 


#### Video - Hardware and Signal processing demonstration
[![Software demonstrations](https://github.com/Ildaron/EEGwithRaspberryPI/blob/master/Supplementary%20files/fig.13.bmp)](https://youtu.be/b-ovJ97vvM)      


#### For beginners
During the measurement, in addition to artifacts caused by muscle activity, be concerned about the increased resistance between the body and the floor. For example, in the picture below, the moment when the feet touch the floor with and without an insulated shoe. Without insulated shoes - increased noise is noticeable




#### Citation  
Soon will be published   
#### Contacts  
ildar.o2010@yandex.ru 

