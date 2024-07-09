print ("ok")
import spidev
import time
from RPi import GPIO
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD)
from gpiozero import LED,Button
from matplotlib import pyplot as plt
#sw1 = Button(26,pull_up=True)#  37
#from gpiozero import LED,Button

import gpiod
button_pin = 26
button_pin_1 = 26
chip = gpiod.Chip("gpiochip4")

button_line = chip.get_line(button_pin)
button_line.request(consumer = "Button", type = gpiod.LINE_REQ_DIR_IN)

button_line_1 = chip.get_line(button_pin_1)
button_line_1.request(consumer = "Button", type = gpiod.LINE_REQ_DIR_IN)

from time import sleep
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=600000

spi.lsbfirst=False
spi.mode=0b01
spi.bits_per_word = 8



spi2 = spidev.SpiDev()  # First ADS1299
spi2.open(0, 1)         # Second ADS1299
spi2.lsbfirst=False
spi2.mode=0b01
spi2.bits_per_word = 8


who_i_am=0x00
config1=0x01
config2=0X02
config3=0X03

reset=0x06
stop=0x0A
start=0x08
sdatac=0x11
rdatac=0x10
wakeup=0x02
rdata = 0x12

ch1set=0x05
ch2set=0x06
ch3set=0x07
ch4set=0x08
ch5set=0x09
ch6set=0x0A
ch7set=0x0B
ch8set=0x0C

data_test= 0x7FFFFF
data_check=0xFFFFFF

def read_byte(register):
 write=0x20
 register_write=write|register
 data = [register_write,0x00,register]
 read_reg=spi.xfer(data)
# GPIO.output(18, True)
 print ("data", read_reg)
 
def send_command(command):
# GPIO.output(18, False)
 send_data = [command]
 com_reg=spi.xfer(send_data)
# GPIO.output(18, True)
# time.sleep(1)
 
def write_byte(register,data):
# GPIO.output(18, False)
 write=0x40
 register_write=write|register
 data = [register_write,0x00,data]
 print (data)
 spi.xfer(data)

def read_byte_1(register):
 write=0x20
 register_write=write|register
 data = [register_write,0x00,register]
 read_reg=spi2.xfer(data)
# GPIO.output(18, True)
 print ("data", read_reg)
 
def send_command_1(command):
# GPIO.output(18, False)
 send_data = [command]
 com_reg=spi2.xfer(send_data)
# GPIO.output(18, True)
# time.sleep(1)
 
def write_byte_1(register,data):
# GPIO.output(18, False)
 write=0x40
 register_write=write|register
 data = [register_write,0x00,data]
 print (data)
 spi2.xfer(data)
 
 

send_command (wakeup)
send_command (stop)
send_command (reset)
send_command (sdatac)

send_command_1 (wakeup)
send_command_1 (stop)
send_command_1 (reset)
send_command_1 (sdatac)


#write_byte (0x14, 0x80) #GPIO
write_byte (config1, 0x96)
write_byte (config2, 0xD4)
write_byte (config3, 0xFF)
write_byte (0x04, 0x00)
write_byte (0x0D, 0x00)
write_byte (0x0E, 0x00)
write_byte (0x0F, 0x00)
write_byte (0x10, 0x00)
write_byte (0x11, 0x00)
write_byte (0x15, 0x20)
#
write_byte (0x17, 0x00)
write_byte (ch1set, 0x00)
write_byte (ch2set, 0x00)
write_byte (ch3set, 0x00)
write_byte (ch4set, 0x00)
write_byte (ch5set, 0x00)
write_byte (ch6set, 0x00)
write_byte (ch7set, 0x00)
write_byte (ch8set, 0x00)

send_command (rdatac)
send_command (start)

write_byte_1 (config1, 0x96)
write_byte_1 (config2, 0xD4)
write_byte_1 (config3, 0xFF)
write_byte_1 (0x04, 0x00)
write_byte_1 (0x0D, 0x00)
write_byte_1 (0x0E, 0x00)
write_byte_1 (0x0F, 0x00)
write_byte_1 (0x10, 0x00)
write_byte_1 (0x11, 0x00)
write_byte_1 (0x15, 0x20)
#
write_byte_1 (0x17, 0x00)
write_byte_1 (ch1set, 0x00)
write_byte_1 (ch2set, 0x00)
write_byte_1 (ch3set, 0x00)
write_byte_1 (ch4set, 0x00)
write_byte_1 (ch5set, 0x00)
write_byte_1 (ch6set, 0x00)
write_byte_1 (ch7set, 0x00)
write_byte_1 (ch8set, 0x00)

send_command_1 (rdatac)
send_command_1 (start)








DRDY=1

result=[0]*27
data_1ch_test = []

figure, axis = plt.subplots(2, 1)
plt.subplots_adjust(hspace=1)

axis_x=0
y_minus_graph=500
y_plus_graph=500
x_minux_graph=5000
x_plus_graph=250
sample_len = 250

axis[0].set_xlabel('Time')
axis[0].set_ylabel('Amplitude')
axis[0].set_title('Data after pass filter')

test_DRDY = 5 

while 1:
    button_state = button_line.get_value()

    if button_state == 1 and button_state_1 == 1:
        test_DRDY = 10
    if test_DRDY == 10 and button_state == 0 and button_state_1 == 0:
        test_DRDY = 0 

        output=spi.readbytes(27)
        output_1=spi2.readbytes(27)
        
        for a in range (3,25,3):
            voltage_1=(output[a]<<8)| output[a+1]
            voltage_1=(voltage_1<<8)| output[a+2]
            convert_voktage=voltage_1|data_test
            if convert_voktage==data_check:
                voltage_1_after_convert=(voltage_1-16777214)
            else:
               voltage_1_after_convert=voltage_1
            channel_num =  (a/3)

            result[int (channel_num)]=round(1000000*4.5*(voltage_1_after_convert/16777215),2)

        data_1ch_test.append(result[1])
        if len(data_1ch_test)==sample_len:
           # print (data_1ch_test)
            
            axis[0].plot(range(axis_x,axis_x+sample_len,1),data_1ch_test, color = '#0a0b0c')  
            axis[0].axis([axis_x-x_minux_graph, axis_x+x_plus_graph, data_1ch_test[50]-y_minus_graph, data_1ch_test[150]+y_plus_graph])
            plt.pause(0.000001)
            
            axis_x=axis_x+sample_len 
            data_1ch_test = []
        
spi.close()
