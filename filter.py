#Program: Filter

'''This program will take an x-y data set, and put a low-pass
filter on it, to sort out fast noise'''

import sys
import os
import numpy as np
import math
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser(description='Filtering out fast noise')

parser.add_argument('filename',help="Input file name (xy)")
parser.add_argument('exp',help="Exposure time")
parser.add_argument('n',help="filter")
args = parser.parse_args()
data = np.loadtxt(args.filename,unpack=True)
size = data[0].shape[-1]
fdat = np.fft.fft(data[1])
freq = np.fft.fftfreq(data[0].shape[-1], d=float(args.exp))
plt.close()
plt.plot(freq[1:250],fdat.real[1:250])
plt.show()
#Now, filter out above some threshold
sampled=fdat
n=float(args.n)
sampled[n:size/2]=0
sampled[size/2+1+n:]=0

newdata = np.fft.ifft(sampled)
t = np.arange(size)*float(args.exp)
p1,=plt.plot(t,newdata.real,label="Filtered, f<%f Hz" % (n/(float(args.exp)*size )) )
p2, =plt.plot(data[0]*float(args.exp),data[1],label="Unfiltered Data")
plt.legend(loc='best')
plt.xlabel('t')
plt.ylabel('Ave. Grey Value')
plt.tight_layout()
plt.show()
