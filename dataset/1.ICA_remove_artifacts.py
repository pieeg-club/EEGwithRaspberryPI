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

fps=fs = 50     # sample rate, Hz
cutoffs = 40
cutoff=2


ch1 = butter_highpass_filter(ch1, cutoff, fps)
ch1  =  butter_lowpass_filter(ch1, cutoffs, fps)

ch2 = butter_highpass_filter(ch2, cutoff, fps)
ch2  =  butter_lowpass_filter(ch2, cutoffs, fps)

ch3 = butter_highpass_filter(ch3, cutoff, fps)
ch3  =  butter_lowpass_filter(ch3, cutoffs, fps)

eeg = np.stack([ch1, ch2, ch3]).T  

# plot original data
plt.subplot(3, 1, 1)
plt.plot(ch1 + 50)
plt.plot(ch2 + 100)
plt.plot(ch3 + 150)
plt.yticks([50, 100, 150], ['ch1', 'ch2', 'ch3'])
plt.ylabel('original data')
print ("ok")

# decompose EEG and plot components
ica = FastICA(n_components=3)
ica.fit(eeg)
components = ica.transform(eeg)

plt.subplot(3, 1, 2)
plt.plot([[np.nan, np.nan, np.nan]])  # advance the color cycler to give the components a different color :)
plt.plot(components + [0.5, 1.0, 1.5])
plt.yticks([0.5, 1.0, 1.5], ['0', '1', '2'])
plt.ylabel('components')

# looks like component #2 (brown) contains the eye blinks
# let's remove them (hard coded)!
components[:, 1] = 0
components[:, 0] = 0
components[:, 0] = 0
#components[0] = 0
#components[1] = 0
# reconstruct EEG without blinks
restored = ica.inverse_transform(components)

plt.subplot(3, 1, 3)
plt.plot(restored + [50, 100, 150])
plt.yticks([50, 100, 150], ['ch1', 'ch2', 'ch3'])
plt.ylabel('cleaned data')
plt.show()
