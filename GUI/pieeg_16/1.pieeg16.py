print("ok")
import spidev
import time
from RPi import GPIO
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD)
from gpiozero import LED,Button
from matplotlib import pyplot as plt
import gpiod

button_pin = 26
chip = gpiod.Chip("gpiochip4")

button_line = chip.get_line(button_pin)
button_line.request(consumer = "Button", type = gpiod.LINE_REQ_DIR_IN)

button_line_1 = chip.get_line(button_pin_1)
button_line_1.request(consumer = "Button", type = gpiod.LINE_REQ_DIR_IN)


from time import sleep

# Initialize two SPI devices
spi1 = spidev.SpiDev()
spi2 = spidev.SpiDev()
spi1.open(0, 0)  # First ADS1299
spi2.open(0, 1)  # Second ADS1299

# Set up SPI parameters for both devices
for spi in [spi1, spi2]:
    spi.max_speed_hz = 600000
    spi.lsbfirst = False
    spi.mode = 0b01
    spi.bits_per_word = 8

# ... (keep all the register definitions as they were)

def read_byte(spi, register):
    write = 0x20
    register_write = write | register
    data = [register_write, 0x00, register]
    read_reg = spi.xfer(data)
    print("data", read_reg)
 
def send_command(spi, command):
    send_data = [command]
    com_reg = spi.xfer(send_data)

def write_byte(spi, register, data):
    write = 0x40
    register_write = write | register
    data = [register_write, 0x00, data]
    print(data)
    spi.xfer(data)

# Initialize both ADS1299 chips
for spi in [spi1, spi2]:
    send_command(spi, wakeup)
    send_command(spi, stop)
    send_command(spi, reset)
    send_command(spi, sdatac)

    write_byte(spi, config1, 0x96)
    write_byte(spi, config2, 0xD4)
    write_byte(spi, config3, 0xFF)
    write_byte(spi, 0x04, 0x00)
    write_byte(spi, 0x0D, 0x00)
    write_byte(spi, 0x0E, 0x00)
    write_byte(spi, 0x0F, 0x00)
    write_byte(spi, 0x10, 0x00)
    write_byte(spi, 0x11, 0x00)
    write_byte(spi, 0x15, 0x20)
    write_byte(spi, 0x17, 0x00)
    
    for ch in range(0x05, 0x0D):  # ch1set to ch8set
        write_byte(spi, ch, 0x00)

    send_command(spi, rdatac)
    send_command(spi, start)

DRDY = 1

result1 = [0] * 27
result2 = [0] * 27
data_1ch_test1 = []
data_1ch_test2 = []

figure, axis = plt.subplots(2, 1)
plt.subplots_adjust(hspace=1)

axis_x = 0
y_minus_graph = 500
y_plus_graph = 500
x_minus_graph = 5000
x_plus_graph = 250
sample_len = 250

for ax in axis:
    ax.set_xlabel('Time')
    ax.set_ylabel('Amplitude')
ax[0].set_title('Data after pass filter - ADS1299 #1')
ax[1].set_title('Data after pass filter - ADS1299 #2')

test_DRDY = 5 

while 1:
    button_state = button_line.get_value()

    if button_state == 1 and button_state_1 == 1:
        test_DRDY = 10
    if test_DRDY == 10 and button_state == 0 and button_state_1 == 0:
        test_DRDY = 0 

        output1 = spi1.readbytes(27)
        output2 = spi2.readbytes(27)
        
        for output, result, data_1ch_test in [(output1, result1, data_1ch_test1), (output2, result2, data_1ch_test2)]:
            for a in range(3, 25, 3):
                voltage_1 = (output[a] << 8) | output[a+1]
                voltage_1 = (voltage_1 << 8) | output[a+2]
                convert_voltage = voltage_1 | data_test
                if convert_voltage == data_check:
                    voltage_1_after_convert = (voltage_1 - 16777214)
                else:
                    voltage_1_after_convert = voltage_1
                channel_num = (a/3)

                result[int(channel_num)] = round(1000000 * 4.5 * (voltage_1_after_convert / 16777215), 2)

            data_1ch_test.append(result[1])
            
            if len(data_1ch_test) == sample_len:
                idx = 0 if data_1ch_test == data_1ch_test1 else 1
                axis[idx].plot(range(axis_x, axis_x + sample_len, 1), data_1ch_test, color='#0a0b0c')  
                axis[idx].axis([axis_x - x_minus_graph, axis_x + x_plus_graph, 
                                data_1ch_test[50] - y_minus_graph, data_1ch_test[150] + y_plus_graph])
                plt.pause(0.000001)
                
                if idx == 1:  # Only increment axis_x after plotting both graphs
                    axis_x = axis_x + sample_len 
                data_1ch_test.clear()
        
spi1.close()
spi2.close()
