#!/usr/bin/env python3
import numpy as np
from functools import partial
from math import trunc, log


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


def fwt(x, *, is_inverse=False):
    length = len(x)

    if length == 1:
        return x

    left = np.zeros(length // 2)
    right = np.zeros(length // 2)

    for index in range(length // 2):
        left[index] = x[index] + x[index + length // 2]
        right[index] = x[index] - x[index + length // 2]

    sub_left = fwt(left, is_inverse=is_inverse)
    sub_right = fwt(right, is_inverse=is_inverse)

    result = np.empty(length)
    divider = 1 if is_inverse else 2
    
    for index in range(length // 2):
        result[index] = sub_left[index] / divider
        result[index + length // 2] = sub_right[index] / divider

    return result


def dwt(x, *, is_inverse=False):
    length = len(x)

    if not log(length, 2).is_integer():
        raise ArithmeticError("Number of doters must be a power of two")

    divider = 1. if is_inverse else 2.
    hadamard_matrix = create_hadamard_matrix(length)

    return np.dot(hadamard_matrix, x) / divider ** log(length, 2)


def create_hadamard_matrix(n):
    power = log(n, 2)

    if not power.is_integer():
        raise ArithmeticError("Number must be a power of two")

    h = np.array([ [1, 1], [1, -1] ])
    hadamard_matrix = np.kron(h, h)
    
    for i in range(1, int(power) - 1):
        hadamard_matrix = np.kron(hadamard_matrix, h)

    return hadamard_matrix


def main():
    pass


if __name__ == '__main__':
    main()