#!/usr/bin/env python
import numpy as np
from scipy.signal import butter, lfilter, freqz, medfilt
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import sys
import itertools
import signal

def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_highpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='high', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y

def butter_highpass_filter(data, cutoff, fs, order=5):
    b, a = butter_highpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y

def intersperse(lst, item):
    result = [item] * (len(lst) * 2 - 1)
    result[0::2] = lst
    return result

def getColumnbyString(matrix, i, gesture_String):
    returnedList = []
    for row in matrix:
        if row[0] == gesture_String:
            returnedList.append(row[i])
    return returnedList        

def getColumnbyIndex(matrix, i):
    returnedList = []
    for row in matrix:
        returnedList.append(row[i])
    return returnedList        

def signal_handler(signal, frame):
        #call here the plotting functions
        print('You pressed Ctrl+C!')
        sys.exit(0)


# Filter requirements.
order = int(float(sys.argv[1]))
sampleSize = int(float(sys.argv[2]))
cutoff = float(sys.argv[3])  # desired cutoff frequency of the filter, Hz
fs = float(sys.argv[4])       # sample rate, Hz  



signal.signal(signal.SIGINT, signal_handler)
print('Press Ctrl+C')
signal.pause()