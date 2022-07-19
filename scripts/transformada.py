import pywt, math
from filters import get_filters
from test_signal_gen import x, y
import matplotlib.pyplot as plt
import numpy as np
from values import q_solved_by_guido, p_solved_by_guido, q_barra_solved_by_guido, p_barra_solved_by_guido 

pattern = [(0, 0.20), (1, 0.50), (2, 0.45), ( 3, 0.85), (4, 0.80), (5, -0.75), (6, 0.25), (7, 0.20), (8, 0.55)]

dec_lo, dec_hi, rec_lo, rec_hi = get_filters(pattern)
# filter_bank = [[i for i in dec_lo.values()], [i for i in dec_hi.values()], [i for i in rec_lo.values()], [i for i in rec_hi.values()]]
filter_bank = [ [i for i in p_solved_by_guido.values()],
                [i for i in q_solved_by_guido.values()], 
                [i for i in p_barra_solved_by_guido.values()], 
                [i for i in q_barra_solved_by_guido.values()]]

class dwt:
    def __init__(self, filter_size, h = None, g = None, h_r = None, g_r = None):
        if h is None:
            self.h = np.random.normal(1,2,filter_size)
        else:
            self.h = h
            self.h_r = h_r
        
        if g is None:
            self.g = np.random.normal(1,2,filter_size)
        else:
            self.g = g
            self.g_r = g_r
        
    def compute(self, input_):
        filter_bank = [self.g, self.h, self.g_r, self.h_r]
        my_wavelet = pywt.Wavelet(name="my_wavelet", filter_bank=filter_bank)
        my_wavelet.biorthogonal = True
        return pywt.dwt(input_, wavelet=my_wavelet)
    
    
    def update_weigths(self, hg, gg, lr = 0.001):
        self.h = self.h - lr*hg
        self.g = self.g - lr*gg

mydwt = dwt(len(filter_bank[0]), filter_bank[1], filter_bank[0], filter_bank[3], filter_bank[2])
cA, cD = mydwt.compute(y)

myWavelet = pywt.Wavelet(name="myWavelet", filter_bank=filter_bank)

signal = pywt.idwt(cA, cD, myWavelet)

phi_d, psi_d, phi_r, psi_r, x = myWavelet.wavefun(5)
phi_x = [i for i in range(0, len(phi_d), 8)]
phi_d_ = [phi_d[i] for i in range(0, len(phi_d), 8)]

# plt.plot(phi_x, phi_d_, 'r-')

psi_x = [i for i in range(0, len(psi_d), 4)]
psi_d_ = [psi_d[i] for i in range(0, len(psi_d), 4)]
# plt.plot(psi_x, psi_d_, 'b-')
# plt.show()

# db1 = pywt.Wavelet(name = 'db1')
# (cA, cD) = pywt.dwt(y, 'db1')
# (cA1, cD1) = pywt.dwt(y, myWavelet)
# (cA, cD) = pywt.dwt(y, myWavelet)
# cA = pywt.downcoef('a', y, myWavelet)

y_ = np.concatenate([cA, cD])

alpha = 0.1
y_1 = [math.exp(-(np.abs(y_[i])**alpha)) for i in range(len(y_))]
y1_max = max(y_1)
x1_max = y_1.index(y1_max)

plt.plot(x1_max, y1_max, 'go')
plt.plot(x1_max, 0, 'go')

x_ = [i for i in range(len(y_))]

plt.plot(x_, y_, 'peru')
plt.plot(x_, y_1, 'b-')
<<<<<<< HEAD:transformada.py

plt.show()
=======
plt.show()
a = 0
>>>>>>> 18da85c9207a976a162de7de34aa206bb618c711:scripts/transformada.py
