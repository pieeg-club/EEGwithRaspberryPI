import spidev
import time
from time import sleep


spi=spidev.SpiDev()
spi.open(0.0)
spi.max_speed_hz=2500000
spi.lsbfirst=False
spicshigh=False
spi.mode=0b01
spi.bits_per_word=8

def write_byte():
 time.sleep(1)
 data = [0x54, 0x00, 0x80]
 spi.xfer(data)
while 1:
 time.sleep(1)
 write.byte()

