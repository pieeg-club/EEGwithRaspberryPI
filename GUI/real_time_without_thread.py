import sys
import ctypes
import numpy as np
from numpy.ctypeslib import ndpointer

from scipy import signal
import matplotlib.pyplot as plt


class GUI:  
    """"""

    def __init__(self, path: str = "./super_real_time_massive.so"):
        np.set_printoptions(threshold=sys.maxsize)
        self.libc = ctypes.CDLL(path)
        self.libc.prepare()

        self.data_for_shift_filter = [[1], [2], [3], [4], [5], [6], [7], [8]]

        self._fps = 250
        self._cutoff = 2
        self._cutoffs = 30

        self._fill_array = 0

    def _receive_data(self, sample_len: int):
        """"""  # TODO add comment
        self.libc.real.restype = ndpointer(
            dtype=ctypes.c_int, shape=(sample_len, 8)
        )
        data = self.libc.real()
        return data

    @staticmethod
    def _butter_highpass(cutoff, fs, order: int =3):
        """"""  # 
        nyq = 0.5 * fs
        normal_cutoff = cutoff / nyq
        b, a = signal.butter(   # TODO Rename a, b
            order, normal_cutoff, btype='high', analog=False
        )
        return b, a

    def _butter_highpass_filter(self, data, cutoff, fs, order=5):
        """"""  # 
        b, a = self._butter_highpass(cutoff=cutoff, fs=fs, order=order)  
        y = signal.filtfilt(b, a, data)
        return y

    @staticmethod
    def _butter_lowpass(cutoff, fs, order=3):
        """"""  # 
        nyq = 0.5 * fs

        normal_cutoff = cutoff / nyq
        b, a = signal.butter(  
            order, normal_cutoff, btype='lowpass', analog=False
        )
        # b, a = signal.butter(8, 0.5, btype='lowpass')
        return b, a

    def _butter_lowpass_filter(self, data, cutoffs, fs, order=5):
        """"""  # TODO add comment
        b, a = self._butter_lowpass(cutoffs, fs, order=order)  #
        y = signal.lfilter(b, a, data)
        return y

    @staticmethod
    def _butter_bandpass(lowcut, highcut, fs, order=5):
        """"""  # 
        nyq = 0.5 * fs
        low = lowcut / nyq
        high = highcut / nyq
        b, a = signal.butter(order, [low, high], btype='band')  # 
        return b, a

    def _butter_bandpass_filter(self, data, lowcut, highcut, fs, order=5):
        """"""  # TODO add comment
        b, a = self._butter_bandpass(lowcut, highcut, fs, order=order)  #
        data = signal.lfilter(b, a, data)
        return data

    def _prepare_data(self, data_array, ch):
        """"""  # TODO add comment
        data = data_array[:, [ch]]
        data = list(data.flatten())
        if self._fill_array == 8:
            data_for_filter = self.data_for_shift_filter[ch] + data
            data_band = self._butter_bandpass_filter(
                data=data_for_filter,
                lowcut=self._cutoff,
                highcut=self._cutoffs,
                fs=self._fps
            )
            data_after_filter = data_band[1000:2000]
            self.data_for_shift_filter[ch] = data
            return data_after_filter
        else:
            self.data_for_shift_filter[ch] = data
            self._fill_array += 1
            data_emtpy_only_one_time = list(range(1000))
            return data_emtpy_only_one_time

    def plot(self):
        """"""  
        sample_len = 1000
        figure, (ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8) = plt.subplots(8, 1, sharex=True)
        axis_x = 0
        y_minus_graph = 500
        y_plus_graph = 500
        x_minux_graph = 5000
        x_plus_graph = 50

        axis_ch = [ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8]

        while True:
            data_array = self._receive_data(sample_len=sample_len)
            for channel in range(8):
                data = self._prepare_data(data_array, channel)
                axis_ch[channel].plot(
                    range(axis_x, axis_x + sample_len),
                    data,
                    color='#0a0b0c'
                )
                axis_ch[channel].axis(
                    [axis_x - x_minux_graph,
                     axis_x + x_plus_graph,
                     data[50] - y_minus_graph,
                     data[500] + y_plus_graph]
                )
            axis_x = axis_x + sample_len
            plt.pause(0.000001)
            plt.draw()


if __name__ == "__main__":
    g = GUI()
    g.plot()
