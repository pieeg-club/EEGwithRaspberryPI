import ctypes
import time
import numpy as np
from numpy.ctypeslib import ndpointer
import sys

np.set_printoptions(threshold=sys.maxsize)

libc = ctypes.CDLL("./super_real_time_massive.so")
libc.prepare()
print("ok")

while 1:
 libc.real.restype = ndpointer(dtype = ctypes.c_int, shape=(200,8))
 print("ok1")
 res = libc.real()
 res= (res[:,[0]])
 print (res.shape)
 res=list(res.flatten())
 print (len(res))
