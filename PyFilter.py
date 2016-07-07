#!/usr/bin/env python
import numpy as np
from scipy.signal import butter, lfilter, freqz, medfilt
from optparse import OptionParser
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
#order = int(float(sys.argv[1]))
#sampleSize = int(float(sys.argv[2]))
#cutoff = float(sys.argv[3])  # desired cutoff frequency of the filter, Hz
#fs = float(sys.argv[4])       # sample rate, Hz  

parser = OptionParser()
parser.add_option("-c", "--cutoff", dest="cutoff",
                  help="cutoff frequency", metavar="CUTOFF")
parser.add_option("-f", "--frequency", dest="fs",
                  help="The sample rate of incoming data", metavar="SAMPLE_RATE")
parser.add_option("-n", "--size", dest="sampleSize",
                  help="The sample size of the incoming data", metavar="SAMPLE_SIZE")
parser.add_option("-o", "--order", dest="order", default=5,
                  help="The filter's order", metavar="ORDER")
parser.add_option("-t", "--type", dest="filterType", default="HPF",
                  help="The type of filter to use, HPF, or LPF.", metavar="FILTER_TYPE")


(options, args) = parser.parse_args()

try: 
	order = int(float(options.order))
except ValueError:
	print("Wrong value for order entered.")
	sys.exit()

try: 
	sampleSize = int(float(options.sampleSize))
except ValueError:
	print("Wrong value for SAMPLE_SIZE entered.")
	sys.exit()

try: 
	cutoff = float(options.cutoff)
except ValueError:
	print("Wrong value for cutoff frequency entered.")
	sys.exit()

try: 
	fs = float(options.fs)
except ValueError:
	print("Wrong value for SAMPLE_RATE entered.")
	sys.exit()

filterType = options.filterType
filterType = filterType.upper()

#if condition to check on the data entered, exit if soemthing is wrong or missing
if filterType not in ["LPF","HPF"]:
	print("Wrong type of filter selected.")
	sys.exit()

if order < 1:
	print("Invalid value for filter's order.")
	sys.exit() 

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
				if filterType == "HPF":
					sampleData[i-1] = butter_highpass_filter(sampleData[i-1], cutoff, fs, order)
				elif filterType == "LPF":
					sampleData[i-1] = butter_lowpass_filter(sampleData[i-1], cutoff, fs, order)
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
