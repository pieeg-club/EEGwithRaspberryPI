### GUI Installation

1.Make sure to have the latest version of PIP installed
``` bash
python -m pip install --upgrade pip
```

2.Install the Python requirements
``` bash
pip install -r requirements.txt
```

3.A Either run the whole script
``` bash
python real_time.py
```

3.B Or run the simpler script
``` bash
python real_time_without_thread.py
```

### Optional: Build C code from scratch

1.If you would like to change C code (data array, etc) then need to compile the static library .so 
For SPI.

``` bash
git clone https://github.com/vsergeev/c-periphery
```

``` bash
mkdir build && cd build
cmake ..
make
```

2.Compiling the .so files

``` bash
gcc -shared -home/pi/Desktop/new_spi/c-periphery-master/src real_time_massive.c /home/pi/Desktop/new_spi/c-periphery-master/build/libperiphery.a -o super_real_time_massive.so
```