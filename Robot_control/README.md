# Control the robot by blinking
![alt tag](![alt tag](https://github.com/Ildaron/EEGwithRaspberryPI/blob/master/Robot_control/Supplementary%20files/fig.1.jpg "general view")​ "general view")​
 "general view")​ "general view")​

Run - robot_control.py   

Connect motor to GPIO in the next points  
GPIO.setup(31, GPIO.OUT)  
GPIO.setup(35, GPIO.OUT)  

set frequency range here - fourier Transform[100:250]
set amplitude here - blinking_value 
the best value must be found experimentally  

Demonstration - the EEG signal (upper graph) converted to a Fourier series (lower graph). We can see in the lower graph for  various frequency ranges, dependence amplitudes from the frequency of  blinking (5 Hz and 3 Hz)
2. We set the threshold to the amplitude and connected two diodes. If the amplitude (lower graph) at a frequency of 1-3 Hz becomes more than the threshold, then the upper LED will light up.
If the amplitude (lower graph)  at a frequency of 3-5 Hz becomes more than the threshold, then the lower LED will light up.
