import numpy as np

def harmonicDetection(pfreq, pmag, pphase, f0, nH, hfreqp, fs):
  # detection of the harmonics from a set of spectral peaks, finds the peaks that are closer
  # to the ideal harmonic series built on top of a fundamental frequency
  # pfreq: peak frequencies, pmag: peak magnitudes, pphase: peak phases
  # f0: fundamental frequency, nH: number of harmonics,
  # hfreqp: harmonic frequencies of previous frame,
  # returns hfreq: harmonic frequencies, hmag: harmonic magnitudes, hphase: harmonic phases
  hfreq = np.zeros(nH)                                 # initialize harmonic frequencies
  hmag = np.zeros(nH)-100                              # initialize harmonic magnitudes
  hphase = np.zeros(nH)                                # initialize harmonic phases
  hf = (f0>0)*(f0*np.arange(1, nH+1))                  # initialize harmonic frequencies
  hi = 0                                               # initialize harmonic index
  if hfreqp == []:
    hfreqp = hf
  while f0>0 and hi<nH and hf[hi]<fs/2:                # find harmonic peaks
    pei = np.argmin(abs(pfreq - hf[hi]))               # closest peak
    dev1 = abs(pfreq[pei] - hf[hi])                    # deviation from perfect harmonic
    dev2 = (abs(pfreq[pei] - hfreqp[hi]) if hfreqp[hi]>0 else fs) # deviation from previous frame
    if dev1<f0/3 or dev2<f0/3:                         # accept peak of deviation is small
      hfreq[hi] = pfreq[pei]                           # harmonic frequencies
      hmag[hi] = pmag[pei]                             # harmonic magnitudes
      hphase[hi] = pphase[pei]                         # harmonic phases
    hi += 1                                            # increase harmonic index
  return hfreq, hmag, hphase

