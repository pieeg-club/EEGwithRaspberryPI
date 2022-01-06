In progress!!! 
Download all folders and run - real_time.py or real_time_without_thread.py

If you would like to change C code (data array, etc) then need to compile the static library .so 
For SPI 
https://github.com/vsergeev/c-periphery
$ mkdir build
$ cd build
$ cmake ..
$ make

and for .so
gcc -shared -home/pi/Desktop/new_spi/c-periphery-master/src real_time_massive.c /home/pi/Desktop/new_spi/c-periphery-master/build/libperiphery.a -o super_real_time_massive.so
