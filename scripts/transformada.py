import pywt, math
from dst.filters import get_filters
from scripts.test_signal_gen import x, y
import matplotlib.pyplot as plt
import numpy as np
from scripts.values import q_solved_by_guido, p_solved_by_guido, q_barra_solved_by_guido, p_barra_solved_by_guido 

#https://colab.research.google.com/github/kastnerkyle/kastnerkyle.github.io/blob/master/posts/wavelets/wavelets.ipynb#scrollTo=XR-xq-pjZeDX

pattern = [(0, 0.20), (1, 0.50), (2, 0.45), ( 3, 0.85), (4, 0.80), (5, -0.75), (6, 0.25), (7, 0.20), (8, 0.55)]
pattern = [0.20, 0.50, 0.45, 0.85, 0.80, -0.75, 0.25, 0.20, 0.55]
dec_lo, dec_hi, rec_lo, rec_hi = get_filters(pattern)
filter_bank = [[i for i in dec_lo.values()], [i for i in dec_hi.values()], [i for i in rec_lo.values()], [i for i in rec_hi.values()]]
# filter_bank = [ [i for i in p_solved_by_guido.values()],
#                 [i for i in q_solved_by_guido.values()], 
#                 [i for i in p_barra_solved_by_guido.values()], 
#                 [i for i in q_barra_solved_by_guido.values()]]



myWavelet = pywt.Wavelet(name="myWavelet", filter_bank=filter_bank)


phi_d, psi_d, phi_r, psi_r, x = myWavelet.wavefun(5)
phi_x = [i for i in range(0, len(phi_d), 1)]
phi_d_ = [phi_d[i] for i in range(0, len(phi_d), 1)]

plt.plot(phi_x, phi_d_, 'r-')
plt.show()

psi_x = [i for i in range(0, len(psi_d), 2)]
psi_d_ = [psi_d[i] for i in range(0, len(psi_d), 2)]
plt.plot(psi_x, psi_d_, 'b-')
plt.show()

# db1 = pywt.Wavelet(name = 'db1')
# (cA, cD) = pywt.dwt(y, 'db1')
# (cA1, cD1) = pywt.dwt(y, myWavelet)
(cA, cD) = pywt.dwt(y, myWavelet, mode='periodization')
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

plt.show()
