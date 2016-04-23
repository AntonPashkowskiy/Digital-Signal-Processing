#!/usr/bin/env python3
import matplotlib.pylab as plt
import numpy as np
import vmsis_dsp

N = 128
dt = np.pi / N
x = np.arange(0.0, N * dt, dt)
signal = np.sin(2 * x) + np.cos(7 * x)


def draw_graphics(walsh_function, title):
    result = walsh_function(signal)
    restored_signal = walsh_function(result, is_inverse = True)

    fig = plt.figure()
    fig.canvas.set_window_title(title)

    original_signal_plot = fig.add_subplot(3, 1, 1)
    original_signal_plot.plot(signal,'r.-')
    original_signal_plot.set_title("Original signal")
    original_signal_plot.grid()

    walsh_signal_plot = fig.add_subplot(3, 1, 2)
    walsh_signal_plot.plot(result,'r.-')
    walsh_signal_plot.set_title(title)
    walsh_signal_plot.grid()

    restored_signal_plot = fig.add_subplot(3, 1, 3)
    restored_signal_plot.plot(restored_signal,'r.-')
    restored_signal_plot.set_title("Restored signal")
    restored_signal_plot.grid()


if __name__ == '__main__':
    draw_graphics(vmsis_dsp.fwt, "Fast walsh transform")
    draw_graphics(vmsis_dsp.dwt, "Discrete walsh transform")

    plt.show()