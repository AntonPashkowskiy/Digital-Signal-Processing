#!/usr/bin/env python3
import numpy as np
from functools import partial

def fft(x, inverse=False):
    def __fft(x):
        N = len(x)

        if N == 1:
            return x
        X_even = __fft(x[0::2])
        X_odd = __fft(x[1::2])
        factor = np.exp(sign * 2j * np.pi * np.arange(N) / N)
        return np.concatenate([X_even + factor[:int(N / 2)] * X_odd,
                               X_even + factor[int(N / 2):] * X_odd])

    N = len(x)
    if inverse:
        sign = 1
        div = 1
    else:
        div = N
        sign = -1
    y = __fft(x)
    return y / div


ifft = partial(fft, inverse=True)


def correlate(x, y):
    if len(x) != len(y):
        raise ArithmeticError('Arguments must have equal length')
    M = np.matrix([np.roll(x, shift) for shift in range(len(x))])
    N = len(x)
    result = (np.dot(M, y) / N).tolist()
    return result[0]

def fold(x, y):
    if len(x) != len(y):
        raise ArithmeticError('Arguments must have equal length')
    M = np.matrix([np.roll(x, -shift) for shift in range(len(x))]) 
    N = len(x)

    temp = y.copy()
    temp.reverse()
    temp = np.roll(temp, 1)
    
    result = (np.dot(M, temp) / N).tolist()
    return result[0]


def correlate_fft(x, y):
    if len(x) != len(y):
        raise ArithmeticError('Arguments must have equal length')
    factors_x = fft(x)
    factors_y = fft(y)
    conjugate_factors_x = [element.conjugate() for element in factors_x]
    
    factors_z = np.multiply(conjugate_factors_x, factors_y)

    return [element.real for element in ifft(factors_z)]


def fold_fft(x, y):
    if len(x) != len(y):
        raise ArithmeticError('Arguments must have equal length')
    factors_x = fft(x)
    factors_y = fft(y)
    
    factors_z = np.multiply(factors_x, factors_y)

    return [element.real for element in ifft(factors_z)]


def main():
    pass


if __name__ == '__main__':
    main()