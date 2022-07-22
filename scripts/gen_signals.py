
from math import floor, cos, sin, pi, exp
import matplotlib.pyplot as plt

def patch_signal_by_steps(x, pattern, func, lower, upper):
    if lower <= x and x <= upper:
        return pattern[floor(x)-lower]
    else:
        return func(x)

def patch_signal_full(x, pattern, func , lower, upper):
    if upper >= len(x) or upper-lower >= len(x) or lower < 0:
        raise Exception('the limits are incorrect')
    y = [func(i) for i in x]
    
    for i in range(lower, upper+1):
        y[i] = pattern[i-lower]
    
    return y

def paper_test_signal(x):
    if x >= 0 and x <= 49:
        return cos((pi *27*x)/8)*sin((pi *75*x)/8)
    else: # 50 <= x <= 63
        return cos((pi *295*x)/32)*sin((pi *105*x)/32)

def example_1(x):
    if x >= 0 and x <= 49:
        return cos((pi *3*x)/8)*sin((pi *25*x)/8)
    else: # 50 <= x <= 63
        return cos((pi *98*x)/32)*sin((pi *33*x)/32)

def example_2(x):
    if x >= 0 and x <= 49:
        return cos((pi *18*x)/8)*sin((pi *60*x)/8)
    else: # 50 <= x <= 63
        return cos((pi *205*x)/32)*sin((pi *75*x)/32)

def example_3(x):
    if x >= 0 and x <= 49:
        return cos((pi *9*x)/8)*sin((pi *45*x)/8)
    else: # 50 <= x <= 63
        return cos((pi *150*x)/32)*sin((pi *75*x)/32)
    
def example_4(x):
    if x >= 0 and x <= 49:
        return cos((pi *2*x)/8)*sin((pi *5*x)/8)
    else: # 50 <= x <= 63
        return cos((pi *30*x)/32)*sin((pi *15*x)/32)


m = [0.20, 0.50, 0.45, 0.85, 0.80, -0.75, 0.25, 0.20, 0.55]
x = [i for i in range(64)]
func = example_4
# y1 = [patch_signal_by_steps(i, m, func, 41, 49) for i in range(64)]
y = patch_signal_full(x, m, func, 41, 49)


# plt.plot(x, y1, 'b-')
plt.plot(x, y, 'r-')
plt.show()
a = 0