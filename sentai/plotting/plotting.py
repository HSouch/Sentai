from matplotlib import pyplot as plt
import numpy as np


"""
========================================
N-Body Plots
========================================
For making general, good looking plots for physics work.
"""


def gen_plot(x, y, xlabel="", ylabel="", err_x=None, err_y=None, show_plot=False, save_plot=False, fit=False,
             show_slope=False, tight_layout=True, line=True,
             filetype="pdf", filename="plot"):
    if line == True:
        l_style = 'dashed'
    else:
        l_style = ''
    """ General x-y plot with optional errors"""
    if err_x is None or err_y is None:
        plt.plot(x, y, color="red", marker="s", linestyle=l_style, mfc='none')
    if err_y is not None and err_x is None:
        plt.errorbar(x, y, yerr=err_y, color="red", marker="s", ecolor="black", linestyle=l_style, mfc='none', capsize=5)
    if err_x is not None and err_y is None:
        plt.errorbar(x, y, xerr=err_x, color="red", marker="s", ecolor="black", linestyle=l_style, mfc='none', capsize=5)
    else:
        plt.errorbar(x, y, xerr=err_x, yerr=err_y, color="red", marker="s", ecolor="black", linestyle=l_style,
                     mfc='none', capsize=5)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    if fit:
        z = np.polyfit(x, y, deg=1)
        p = np.poly1d(z)
        plt.plot(x, p(x), color="red")
        if show_slope:
            x_loc = ((max(x) - min(x)) / 2) + min(x)
            y_loc = max(y)
            slope = str(p(1) - p(0))
            if len(slope) > 8:
                slope = slope[0:7]
            plt.text(x_loc, y_loc, "m=" + slope)
    if tight_layout:
        plt.tight_layout()
    if show_plot:
        plt.show()
    if save_plot:
        plt.savefig(filename + "." + filetype)