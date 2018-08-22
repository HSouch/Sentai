from matplotlib import pyplot as plt


"""
========================================
N-Body Plots
========================================
For making general, good looking plots for physics work.
"""


def gen_plot(x, y, xlabel="", ylabel="", err=None, show_plot=False, save_plot=False, filetype="pdf", filename="plot"):
    """ General x-y plot with optional errors"""
    if err is None:
        plt.plot(x, y, color="red", marker="s", linestyle="solid", mfc='none')
    else:
        plt.errorbar(x, y, err, color="red", marker="s", ecolor="black", linestyle="dashed", mfc='none', capsize=5)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.tight_layout()
    if show_plot:
        plt.show()
    if save_plot:
        plt.savefig(filename + "." + filetype)