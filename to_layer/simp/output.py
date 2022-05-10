import os
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.ticker import MaxNLocator
from pathlib import Path


class SimpOutput:
    fig = None
    ax_l = None
    ax_r = None

    it_container = []
    obj_container = []

    design_shape = None

    def __init__(self, name: str = "test"):

        self.name = name

        self.it_container = []
        self.obj_container = []

        self.fig, (self.ax_l, self.ax_r) = plt.subplots(nrows=1, ncols=2, figsize=(8, 4))
        self.ax_l.set_title("Flexibility $c$")
        self.ax_l.set_ylabel("obj. value $c$")
        self.ax_l.set_xlabel("Iteration")

        self.ax_r.set_title("Shape")
        self.ax_r.set_axis_off()

        self.fig.show()

    def get_image_data(self):
        return self.it_container, self.obj_container

    def close_figure(self):
        plt.close(self.fig)

    def update(self, iteration, obj, x, change):

        print("it: {}\tobj: {}\tchange: {}".format(iteration, obj, change))

        self.it_container.append(iteration)
        self.obj_container.append(obj)

        self.ax_l.plot(self.it_container, self.obj_container, c="r")
        self.ax_l.xaxis.set_major_locator(MaxNLocator(integer=True))

        x = x.reshape(self.design_shape)
        x = x.T
        x = np.flip(x, 0)
        self.ax_r.imshow(x, cmap="binary", vmin=0, vmax=1)

        self.fig.show()
        plt.pause(0.1)


if __name__ == "__main__":
    out = SimpOutput()
    out.design_shape = (4, 4)
    for i in range(50):

        out.update(i, 1000 * np.random.rand(), np.random.rand(16), 1)
