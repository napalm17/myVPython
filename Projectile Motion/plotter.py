from vpython import *

j = 1

class Plot:
    def __init__(self):     # Create a graph for every projectile.
        global j
        graph(title=f"projectile {j}", xtitle="t", ytitle="q")
        self.plots = [gcurve(color=col, label=q) for q, col in zip(["x", "y", "z"], [color.red, color.blue, color.green])]
        j +=1
        
    def update_plot(self, t, q):    # Plot projectile's motion in every dimension.
        for i, plot in zip(range(3), self.plots):
            plot.plot(pos=(t, q[i]))
