import spidev
import time
from RPi import GPIO
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
from time import sleep
GPIO.cleanup()

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=2500000
spi.lsbfirst=False
spi.cshigh=False
spi.mode=0b01
spi.bits_per_word = 8

config1=0x01
config2=0X02
config3=0X03

start=0x08
sdatac=0x11
rdatac=0x10
ch1set=0x05
ch2set=0x06
ch3set=0x07
ch4set=0x08
ch5set=0x09
ch6set=0x0A
ch7set=0x0B
ch8set=0x0C

def read_byte(register):
 print ("write_regsiter")
 write=0x20
 register_write=write|register
 data = [register_write,0x00,register]
 read_reg=spi.xfer(data)
# time.sleep(1)
 print ("data", read_reg)
 
def send_command(command):
 print ("command")
 send_data = [command]
 print ("send_data", send_data)
 com_reg=spi.xfer(send_data)
 time.sleep(1)
def write_byte(register,data):
 print ("write_regsiter")
 write=0x40
 register_write=write|register
 data = [register_write,0x00,data]
 spi.xfer(data)
# time.sleep(1)

send_command (sdatac)
write_byte (0x14, 0x80) #GPIO
write_byte (config1, 0x96)
write_byte (config2, 0xD4)
write_byte (config3, 0xE0)
write_byte (0x04, 0x00)
write_byte (0x0D, 0xFF)
write_byte (0x0E, 0x00)
write_byte (0x0F, 0x00)
write_byte (0x10, 0x00)
write_byte (0x11, 0x00)
write_byte (0x15, 0x20)
write_byte (0x17, 0x00)
write_byte (ch1set, 0x40)
write_byte (ch2set, 0x40)
read_byte(ch1set)

#time.sleep(1)
send_command (rdatac)
#time.sleep(1)
send_command (start)
#time.sleep(1)

DRDY=1
lenght = [0,1,2,3,4]
byte=[0,1,2]
test=[0x00,0x00,0x00]
output=[0,0,0,0,0]



while 1:  
# if HAL_GPIO_WritePin(GPIOD, CS_Pin, GPIO_PIN_RESET);
 if GPIO.input(26) == GPIO.HIGH:
 #if (GPIO.input(26) == 1):
 #GPIO.input(2)==0:
  DRDY=0
  #print ("DRDY high")
 if GPIO.input(26) == GPIO.LOW & DRDY==0:
 #if (GPIO.input(11)==1) ＆ DRDY==0): 
  DRDY=1
  #print ("read_data")
  for a in lenght:
   output[a]=spi.xfer(test)
  print ("OUTPUT", output[1])
   # for number_bytes in byte:
    






  

