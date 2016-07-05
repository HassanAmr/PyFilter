#!/usr/bin/env python
import numpy as np
from scipy.signal import butter, lfilter, freqz, medfilt
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import sys
import itertools
import signal

def signal_handler(signal, frame):
        print('You pressed Ctrl+C!')
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)
print('Press Ctrl+C')
signal.pause()