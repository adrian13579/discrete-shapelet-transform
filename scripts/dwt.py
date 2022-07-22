from numpy.lib.stride_tricks import as_strided
import numpy as np

def polyphase_core(x, m, f):
    #x = input data
    #m = decimation rate
    #f = filter
    #Force it to be 1D
    x = x.ravel()
    #Hack job - append zeros to match decimation rate
    if x.shape[0] % m != 0:
        x = np.append(x, np.zeros((m - x.shape[0] % m,)))
    if f.shape[0] % m != 0:
        f = np.append(f, np.zeros((m - f.shape[0] % m,)))
    polyphase = p = np.zeros((m, (x.shape[0] + f.shape[0]) / m), dtype=x.dtype)
    p[0, :-1] = np.convolve(x[::m], f[::m])
    #Invert the x values when applying filters
    for i in range(1, m):
        p[i, 1:] = np.convolve(x[m - i::m], f[i::m])
    return p

def wavelet_lp(data, ntaps=4):
    #type == 'haar':
    f = np.array([1.] * ntaps)
    return np.sum(polyphase_core(data, 2, f), axis=0)

def wavelet_hp(data, ntaps=4):
    #type == 'haar':
    if ntaps % 2 is not 0:
        raise ValueError("ntaps should be even")
    half = ntaps // 2
    f = np.array(([-1.] * half) + ([1.] * half))
    return np.sum(polyphase_core(data, 2, f), axis=0)

def wavelet_filterbank(n, data):
    #Create and store all coefficients to level n
    x = data
    all_lp = []
    all_hp = []
    for i in range(n):
        c = wavelet_lp(x)
        x = wavelet_hp(x)
        all_lp.append(c)
        all_hp.append(x)
    return all_lp, all_hp

def zero_crossing(x):
    x = x.ravel()
    #Create an X, 2 array of overlapping points i.e.
    #[1, 2, 3, 4, 5] becomes
    #[[1, 2],
    #[2, 3],
    #[3, 4],
    #[4, 5]]
    o = as_strided(x, shape=(x.shape[0] - 1, 2), strides=(x.itemsize, x.itemsize))
    #Look for sign changes where sign goes from positive to negative - this is local maxima!
    #Negative to positive is local minima
    return np.where((np.sum(np.sign(o), axis=1) == 0) & (np.sign(o)[:, 0] == 1.))[0]

def peak_search(hp_arr, arr_max):
    #Given all hp coefficients and a limiting value, find and return all peak indices
    zero_crossings = []
    for n, _ in enumerate(hp_arr):
        #2 ** (n + 1) is required to rescale due to decimation by 2 at each level
        #Also remove a bunch of redundant readings due to clip using np.unique
        zero_crossings.append(np.unique(np.clip(2 ** (n + 1) * zero_crossing(hp_arr[n]), 0, arr_max)))

    #Find refined estimate for each peak
    peak_idx = []
    for v in zero_crossings[-1]:
        v_itr = v
        for n in range(len(zero_crossings) - 2, 0, -1):
            v_itr = find_nearest(v_itr, zero_crossings[n])
        peak_idx.append(v_itr)
    #Only return unique answers
    return np.unique(np.array(peak_idx, dtype='int32'))
    
def find_nearest(v, x):
    return x[np.argmin(np.abs(x - v))]
    
def peak_detect(data, depth):
    if depth == 1:
        raise ValueError("depth should be > 1")
    #Return indices where peaks were found
    lp, hp = wavelet_filterbank(depth, data)
    return peak_search(hp, data.shape[0] - 1)