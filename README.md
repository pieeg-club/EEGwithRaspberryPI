# The easiest way to neuroscience world with PIEEG (In progress) 
[![Tweet](https://img.shields.io/twitter/url/http/shields.io.svg?style=social)](https://twitter.com/intent/tweet?text=DIY%20Brain-Computer%20%20interface%20ironbci%20&url=https://github.com/Ildaron/ironbci&hashtags=RaspberryPI,EEG,python,opensource)

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
This also applies to the monitor. Use only a monitor that is powered by the RaspberryPI.  
![alt tag](https://github.com/Ildaron/EEGwithRaspberryPI/blob/master/Supplementary%20files/Fig.7.jpg "general view")​

#### Device pinout  
Shiled connceted with raspbberryPI only in the netxt points     
  43  +5V  
  44  GND  
  37  MOSI  
  34  MISO  
  35  CLKL  
  36  CS  
  
#### Noise measure
In register Ch1 with the address 0x05 set - 0x01 for internal short circuit (via timeflux)  
![alt tag](https://github.com/Ildaron/EEGwithRaspberryPI/blob/master/Supplementary%20files/noise/img_2.jpg "general view")​
In register Ch1 with the address 0x05 set - 00 for  short circuit used the cable (via timeflux)    
![alt tag](https://github.com/Ildaron/EEGwithRaspberryPI/blob/master/Supplementary%20files/noise/img1.jpg "general view")​
Chewing artifact 4-3-2-1
![alt tag](https://github.com/Ildaron/EEGwithRaspberryPI/blob/master/Supplementary%20files/Fig.4.jpg "general view")​  
Blinking artifact, after Chewing
![alt tag](https://github.com/Ildaron/EEGwithRaspberryPI/blob/master/Supplementary%20files/Fig.6.jpg "general view")​  

#### Description of the code  
For signal processing can be used Python scripts or Brainflow   


#### Video - Hardware and Signal processing demonstration
(Soon be added)

#### For beginners
During the measurement, in addition to artifacts caused by muscle activity, be concerned about the increased resistance between the body and the floor. For example, in the picture below, the moment when the feet touch the floor with and without an insulated shoe. Without insulated shoes - increased noise is noticeable
![alt tag](https://github.com/Ildaron/EEGwithRaspberryPI/blob/master/Supplementary%20files/Fig.5.jpg "general view")​  



#### Citation  
Soon will be published   
#### Contacts  
ildar.o2010@yandex.ru 

