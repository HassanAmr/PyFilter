#!/usr/bin/env python
import numpy as np
from scipy.signal import butter, lfilter, freqz, medfilt
import sys
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




# Filter requirements.
order = int(float(sys.argv[1]))
sampleSize = int(float(sys.argv[2]))
cutoff = float(sys.argv[3])  # desired cutoff frequency of the filter, Hz
fs = float(sys.argv[4])       # sample rate, Hz  


#try:
#	opts, args = getopt.getopt(argv,"hc:o:n:",["ifile=","ofile="])
#except getopt.GetoptError:
#	print 'PyFilter.py -i <inputfile> -o <outputfile>'
#	sys.exit(2)
#for opt, arg in opts:
#	if opt == '-h':
#		print 'test.py -i <inputfile> -o <outputfile>'
#		sys.exit()
#	elif opt in ("-c", "--cutoff"):
#		inputfile = arg
#	elif opt in ("-o", "--ofile"):
#		outputfile = arg


print("starting...")

for line in sys.stdin:
	if line == '\n':
		print('end line')
	else:
		sample = line.split()	
		for i in range(1,len(sample)): 
 			print(sample[i]+'\n')
	#whatever
