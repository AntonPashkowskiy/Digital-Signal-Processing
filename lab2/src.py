#!/usr/bin/env python3
from numpy import arange, pi, sin, cos, angle, fft, abs
from matplotlib.pyplot import show, figure


N = 64
Δt = pi / N
x = arange(0.0, N * Δt, Δt)
y1 = sin(2 * x)
y2 = cos(2 * x)


def draw_chart(fig, chart_name, x, y, quarter = 1):
    s = fig.add_subplot(2, 2, quarter)
    s.plot(x, y, 'r.-')
    s.set_title(chart_name)
    s.set_xlabel('x')
    s.set_ylabel('y(x)')
    s.grid(True)


def show_original_signals(fig):
    draw_chart(fig, 'sin(2x)', x, y1, 1)
    draw_chart(fig, 'cos(2x)', x, y2, 2)


def main():
    fig = figure()
    fig.canvas.set_window_title('Исходные сигналы.')
    show_original_signals(fig)
    show()


if __name__ == '__main__':
    main()