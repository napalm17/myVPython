from vpython import *

j = 1



class Plot:
    def __init__(self):     # Create a graph for every projectile.
        global j
        g1 = graph(ytitle="position [m]", background=color.black)
        self.plots = [gcurve(color=col, label=q) for q, col in zip(["x", "y"], [color.red, color.cyan, color.green])]

        g2 = graph(xtitle="time [s]", ytitle="angle [deg]", background=color.black)
        self.angle_plot = gcurve(color=color.magenta)

        j += 1
        
    def update_plot(self, t, q):    # Plot projectile's motion in every dimension.
        self.plots[0].plot(pos=(t, q[0]))
        self.plots[1].plot(pos=(t, q[1] + 1))
        self.angle_plot.plot(pos=(t, degrees(asin(q[0]))))
