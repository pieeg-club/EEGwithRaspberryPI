# Control the robot by blinking

For example, discrete output channels from GPIO can be connected directly or through a relay to the control panel of radio-controlled toy robots.  
![alt tag](https://github.com/Ildaron/EEGwithRaspberryPI/blob/master/Robot_control/Supplementary%20files/fig.1.jpg "general view")

Run - robot_control.py   

Connect motor to GPIO in the next points  
GPIO.setup(31, GPIO.OUT)  
GPIO.setup(35, GPIO.OUT)  

set frequency range here - "fourier Transform[0:3]"  
set amplitude here - "blinking_value"   
the best value must be found experimentally    

![alt tag](https://github.com/Ildaron/EEGwithRaspberryPI/blob/master/Robot_control/Supplementary%20files/fig.2.jpg "general view")

(upper graph) - EEG signal through pass filter 1-30 Hz. Lower graph - EEG signal received through the Fast Fourier Transform (the part circled in purple from the graph above). The red line is the setting for turning on the LED, green lines are the frequency range in which we monitor the signal amplitude. (lower graph) – LED circled in blue, output - 31 for GPIO.setmode (GPIO.BOARD)    


We can see in the lower graph for  various frequency ranges, dependence amplitudes from the frequency of  blinking (5 Hz and 3 Hz)
We can set the threshold to the amplitude and connected two diodes. If the amplitude (lower graph) at a frequency of 1-3 Hz becomes more than the threshold, then the upper LED will light up.
If the amplitude (lower graph)  at a frequency of 3-5 Hz becomes more than the threshold, then the lower LED will light up.  
