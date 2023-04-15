# Create a 2D line plot with custom label.
#
import pyvista
chart = pyvista.Chart2D()
plot = chart.line([0, 1, 2], [2, 1, 3])
plot.label = "My awesome plot"
chart.show()
