# Set the bar plot's color to red.
#
import pyvista
chart = pyvista.Chart2D()
plot = chart.bar([1, 2, 3], [2, 1, 3])
plot.color = 'r'
chart.show()
