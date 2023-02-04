import numpy as np
import scipy.signal as sps
from sklearn.decomposition import FastICA
import matplotlib.pyplot as plt
import pandas as pd
from scipy import signal

data = pd.read_excel("data.xlsx")
ch1 = data["ch1"]
ch2 = data["ch2"]
ch3 = data["ch3"]
ch4 = data["ch4"]
ch5 = data["ch5"]
ch6 = data["ch6"]
ch7 = data["ch7"]
ch8 = data["ch8"]

def butter_highpass(cutoff, fs, order=3):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = signal.butter(order, normal_cutoff, btype='high', analog=False)
    return b, a
def butter_highpass_filter(data, cutoff, fs, order=5):
    b, a = butter_highpass(cutoff, fs, order=order)
    y = signal.filtfilt(b, a, data)
    return y
def butter_lowpass(cutoffs, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = signal.butter(order, normal_cutoff, btype='low', analog=False)
    return b, a
def butter_lowpass_filter(data, cutoffs, fs, order=5):
    b, a = butter_lowpass(cutoffs, fs, order=order)
    y = signal.lfilter(b, a, data)
    return y

fps=fs = 25     # sample rate, Hz
cutoffs = 60
cutoff=2


ch1 = butter_highpass_filter(ch1, cutoff, fps)
ch1  =  butter_lowpass_filter(ch1, cutoffs, fps)
ch2 = butter_highpass_filter(ch2, cutoff, fps)
ch2  =  butter_lowpass_filter(ch2, cutoffs, fps)
ch3 = butter_highpass_filter(ch3, cutoff, fps)
ch3  =  butter_lowpass_filter(ch3, cutoffs, fps)
ch4 = butter_highpass_filter(ch4, cutoff, fps)
ch4  =  butter_lowpass_filter(ch4, cutoffs, fps)
ch5 = butter_highpass_filter(ch5, cutoff, fps)
ch5  =  butter_lowpass_filter(ch5, cutoffs, fps)
ch6 = butter_highpass_filter(ch6, cutoff, fps)
ch6  =  butter_lowpass_filter(ch6, cutoffs, fps)
ch7 = butter_highpass_filter(ch7, cutoff, fps)
ch7  =  butter_lowpass_filter(ch7, cutoffs, fps)
ch8 = butter_highpass_filter(ch8, cutoff, fps)
ch8  =  butter_lowpass_filter(ch8, cutoffs, fps)

eeg = np.stack([ch1, ch2, ch3, ch4, ch5, ch6, ch7, ch8]).T  

# plot original data
plt.subplot(8, 1, 1)
plt.plot(ch1 + 50)
plt.plot(ch2 + 100)
plt.plot(ch3 + 150)
plt.plot(ch4 + 200)
plt.plot(ch5 + 250)
plt.plot(ch6 + 300)
plt.plot(ch7 + 350)
plt.plot(ch8 + 400)

plt.yticks([50, 100, 150, 200, 250, 300, 350, 400], ['ch1', 'ch2', 'ch3', 'ch4', 'ch5', 'ch6', 'ch7', 'ch8'])

plt.ylabel('original data')

# decompose EEG and plot components
ica = FastICA(n_components=8)
ica.fit(eeg)
components = ica.transform(eeg)

plt.subplot(8, 1, 2)
plt.plot([[np.nan, np.nan, np.nan,np.nan, np.nan, np.nan,np.nan, np.nan]])
plt.plot(components + [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0])
plt.yticks([0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0], ['0', '1', '2','3', '4', '5','6', '7'])
plt.ylabel('components')


components[:, 6] = 0
components[:, 5] = 0
components[:, 4] = 0
components[:, 3] = 0
components[:, 2] = 0
components[:, 1] = 0
components[:, 0] = 0

#components[0] = 0
#components[1] = 0
# reconstruct EEG without blinks
restored = ica.inverse_transform(components)

plt.subplot(3, 1, 3)
plt.plot(restored + [50, 100, 150, 200, 250, 300, 350, 400])
plt.yticks([50, 100, 150, 200, 250, 300, 350, 400], ['ch1', 'ch2', 'ch3', 'ch4', 'ch5', 'ch6', 'ch7', 'ch8', ])
plt.ylabel('cleaned data')
plt.show()
