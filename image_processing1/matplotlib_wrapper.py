"""
This module contains  base class for matplotlib subplots painters and
specific realizations of subplots painters.

Go to the main section to see an example of using subplots painter
"""

import matplotlib.pylab as plt
import abc


class _MatplotlibSubplotsPainter(metaclass=abc.ABCMeta):
    """ Base class for specific matplotlib class painter.
    """

    def __init__(self, description, grid_size):
        """ Initialize data and create subplot objects.
        """

        self._description = description
        self._width, self._height = grid_size

        # initialize subplots
        self._figure, subplots = plt.subplots(self._width, self._height)
        self._figure.canvas.set_window_title(description)
        self._subplots = subplots.ravel()

    @abc.abstractmethod
    def append_plot(self, *args):
        """ Should append new graphic on the grid.
        """

        pass

    @abc.abstractmethod
    def show(self):
        """ Should show graphic.
        """

        pass


class HistogramPainter(_MatplotlibSubplotsPainter):
    """ Specific matplotlib histogram painter.
    """

    def __init__(self, description, grid_size):
        """ Initialize histogram painter.
        """

        self.__current_position = 0
        super().__init__(description, grid_size)

    def append_plot(self, description, data, *args, **kwargs):
        """
        Initialize histogram with data and set them on the grid.

        You can customize drawing plot with special positional and keywords arguments.
        For find information about arguments see matplotlib documentation:
        http://matplotlib.org/api/pyplot_api.html?highlight=hist#matplotlib.pyplot.hist
        """

        if self.__current_position >= self._width * self._height:
            raise OverflowError("Overflowing grid.")

        plot = self._subplots[self.__current_position]

        plot.grid()
        plot.set_title(str(description))
        plot.hist(data, *args, **kwargs)

        self.__current_position += 1

    @property
    def current_position(self):
        return self.__current_position

    def show(self):
        """ Display figure.
        """

        plt.tight_layout()
        plt.show()


class BarChartPainter(_MatplotlibSubplotsPainter):
    """ Specific matplotlib bar chart painter.
    """

    def __init__(self, description, grid_size):
        """ Initialize bar chart painter.
        """

        self.__current_position = 0
        super().__init__(description, grid_size)

    def append_plot(self, description, data, *args, **kwargs):
        """
        Initialize bar chart with data and set them on the grid.

        You can customize drawing plot with special positional and keywords arguments.
        For find information about arguments see matplotlib documentation:
        http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.bar
        """

        if self.__current_position >= self._width * self._height:
            raise OverflowError("Overflowing grid.")

        plot = self._subplots[self.__current_position]

        plot.grid()
        plot.set_title(str(description))
        plot.bar(range(len(data)), data, *args, **kwargs)

        self.__current_position += 1

    def show(self):
        """ Display figure.
        """

        plt.tight_layout()
        plt.show()

if __name__ == '__main__':
    # Example of using HistogramPainter

    import numpy as np

    painter = HistogramPainter("My histogram example", (3, 3))

    for index in range(8):
        data = np.random.random_sample(1000)
        painter.append_plot(index, data)

    data = np.random.random_sample(1000)
    painter.append_plot("Special arguments", data, color="green", orientation='horizontal')

    painter.show()
