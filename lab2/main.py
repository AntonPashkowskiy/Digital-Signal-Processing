#!/usr/bin/env python3
from src import draw_chart, show_original_signals, y1, y2, x
from vmsis_dsp import correlate, fold, correlate_fft, fold_fft
from matplotlib.pyplot import show, figure


y1 = y1.tolist()
y2 = y2.tolist()


def show_base_results():
    fig = figure()
    fig.canvas.set_window_title('Свёртка и корреляция')
    show_original_signals(fig)

    fold_results = fold(y1, y2)
    correlation_results = correlate(y1, y2)

    draw_chart(fig, 'fold(x)', x, fold_results, 3)
    draw_chart(fig, 'correlation(x)', x, correlation_results, 4)


def show_fft_results():
    fig = figure()
    fig.canvas.set_window_title('Свёртка и корреляция с БПФ')
    show_original_signals(fig)

    fold_results = fold_fft(y1, y2)
    correlation_results = correlate_fft(y1, y2)

    draw_chart(fig, 'fold_fft(x)', x, fold_results, 3)
    draw_chart(fig, 'correlation_fft(x)', x, correlation_results, 4)
    

def main():
    show_base_results()
    show_fft_results()
    show()


if __name__ == '__main__':
    main()