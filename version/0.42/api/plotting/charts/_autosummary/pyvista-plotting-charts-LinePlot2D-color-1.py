# Set the 2D line plot's color to red.
#
import pyvista
chart = pyvista.Chart2D()
plot = chart.line([0, 1, 2], [2, 1, 3])
plot.color = 'r'
chart.show()
