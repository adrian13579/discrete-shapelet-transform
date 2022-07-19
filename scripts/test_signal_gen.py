import math
import numpy as np
import matplotlib.pyplot as plt
# from scipy.interpolate import make_interp_spline

# m = [(0, 0.20), (1, 0.50), (2, 0.45), ( 3, 0.85), (4, 0.80), (5, -0.75), (6, 0.25), (7, 0.20), (8, 0.55)]
m = [0.20, 0.50, 0.45, 0.85, 0.80, -0.75, 0.25, 0.20, 0.55]
x0 = np.arange(0, 41, 1)
x = [i for i in x0]
x1 = np.arange(41, 50)
x += [i for i in x1]
x2 = np.arange(50, 63+1, 1)
x += [i for i in x2]

def signal(x):
    if x >= 0 and x <= 40:
        return math.cos((math.pi *27*x)/8)*math.sin((math.pi *75*x)/8)
    elif x >= 41 and x <= 49:
        return m[int(x)%8]
    else: # 50 <= x <= 63
        return math.cos((math.pi *295*x)/32)*math.sin((math.pi *105*x)/32)

y = [signal(i) for i in x]
y0 = [signal(i) for i in x0]
# x0_y0_spline = make_interp_spline(x0, y0)
# x0_ = np.linspace(x0[0], x0[-1], 1000)
# y0_ = x0_y0_spline(x0_)
y1 = [signal(i) for i in x1]
y2 = [signal(i) for i in x2]

print(signal(15))
# plt.plot(x0_, y0_, 'b-')
# plt.plot(x0, y0, 'b-')
# plt.plot(x1, y1, 'r-')
# plt.plot(x2, y2, 'b-')
# plt.plot(x, y, 'r-')
# plt.show()