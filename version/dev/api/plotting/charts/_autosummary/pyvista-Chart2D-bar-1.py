# Generate a bar plot.
#
import pyvista as pv
chart = pv.Chart2D()
plot = chart.bar([0, 1, 2], [2, 1, 3])
chart.show()
