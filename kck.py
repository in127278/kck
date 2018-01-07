from __future__ import division
from pylab import *
from numpy import *
from scipy import *
import scipy.io.wavfile
import glob
def main_loop(x,signal,file):
    try:
        signal = [s[0] for s in signal]     
    except IndexError:
        x
    window=np.hamming(len(signal))
    signal=signal*window
    signal=fft(log(abs(fft(signal)))) #*2/len(signal)
    i=argmax(signal[1:])
    i+=1
    print(int(signal[i]),file)
#    k = arange(len(signal))
 #   y = len(signal)/x  # where fs is the sampling frequency
  #  frqLabel = k/y
    return int(signal[i])
if __name__ == "__main__":
    files = glob.glob("train/*.wav")
    for file in files:
        try:
            x, signal = scipy.io.wavfile.read(file)
            main_loop(x,signal,file)
        except ValueError:
            continue
