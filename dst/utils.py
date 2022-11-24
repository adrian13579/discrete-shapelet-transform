import numpy as np
import math


def S(x, alpha=0.1):
    """
    Experimental measure of similarity,emphasizing
    the presence of zeros in the DST-II
    """
    y = np.zeros_like(x, dtype="float")
    if len(x.shape) == 2:
        for i in range(x.shape[0]):
            for j in range(x.shape[1]):
                y[i][j] = math.exp(-(math.fabs(x[i][j]) ** alpha))
    elif len(x.shape) == 1:
        for i in range(x.shape[0]):
            y[i] = math.exp(-(math.fabs(x[i]) ** alpha))
    else:
        raise Exception(f"Incorrect vector shape: {x.shape}")

    return y

def indexes(array):
    return [(index, value) for index, value in enumerate(array)]

def get_over(array, threshold):
    return [x for x in array if x[1] >= threshold]


