from matplotlib.pyplot import subplot, show, plot

"""
========================================
N-Body Plots
========================================
For plotting n-body simulations in a 3-Dimensional environment.
"""


def n_body_plot(positions, convert_to=1):
    fig = subplot(111, projection='3d')
    for position_list in positions:
        xs, ys, zs = [], [], []
        for vector in position_list:
            xs.append(vector.x / convert_to)
            ys.append(vector.y / convert_to)
            zs.append(vector.z / convert_to)
        fig.plot(xs, ys, zs)

    show()
