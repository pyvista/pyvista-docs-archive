# Create a area plot.
#
import pyvista
chart = pyvista.Chart2D()
plot = chart.area([0, 1, 2], [0, 0, 1], [1, 3, 2])
chart.show()
#
# Hide it.
#
plot.toggle()
chart.show()
