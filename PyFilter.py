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

data = []
ws = ' ' #the white space character to be used
for i in range(0,sampleSize + 1): #the extra 1 is for the label
	tempArr = []
	data.append(tempArr)

for line in sys.stdin:
	if line == '\n':
		sampleData = []
		label = []
		strLine = ""
		for i in range(0, sampleSize + 1):
			#skip the label array when filtering
			if i > 0:
				sampleData.append([float(item) for item in data[i]])
				sampleData[i-1] = medfilt(sampleData[i-1])
				sampleData[i-1] = butter_highpass_filter(sampleData[i-1], cutoff, fs, order)
			else:
				label = data[i]
			data[i] = []
		for i in range(0, len(sampleData[0])):
			strLine += label[i] + ws
			for j in range (0, sampleSize):
				strLine += "{:.6f}".format(sampleData[j][i]) + ws
			print(strLine)
			strLine = ""
		print()
	else:
		sample = line.split()	
		for i in range(0,len(sample)): 
 			data[i].append(sample[i])
