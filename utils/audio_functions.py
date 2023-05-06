from scipy.io import wavfile
import numpy as np
import pandas as pd


def envelope(y,rate,thresold):
  mask = []
  y = pd.Series(y).apply(np.abs)
  y_mean = y.rolling(window = int(rate/10), min_periods = 1, center = True).mean()
  for mean in y_mean:
    if mean>thresold:
      mask.append(True)
    else: 
      mask.append(False)
  return mask

class Config:
  def __init__(self, mode = "conv", nfilt = 26, nfeat = 13, nfft = 512, rate = 12000):
    self.mode = mode
    self.nfilt = nfilt
    self.nfeat = nfeat
    self.nfft = nfft
    self.rate = rate
    self.step = int(rate/10)