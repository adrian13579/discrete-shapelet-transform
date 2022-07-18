import pywt, math
from filters import get_filters

pattern = [(0, 0.20), (1, 0.50), (2, 0.45), ( 3, 0.85), (4, 0.80), (5, -0.75), (6, 0.25), (7, 0.20), (8, 0.55)]

dec_lo, dec_hi, rec_lo, rec_hi = get_filters(pattern)
filter_bank = [[i for i in dec_lo.values()], [i for i in dec_hi.values()], [i for i in rec_lo.values()], [i for i in rec_hi.values()]]

myWavelet = pywt.Wavelet(name="myWavelet", filter_bank=filter_bank)
a = 0