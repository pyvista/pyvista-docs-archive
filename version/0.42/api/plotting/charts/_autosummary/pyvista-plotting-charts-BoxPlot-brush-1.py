# Use a custom texture for the box plot's brush object.
#
import pyvista
from pyvista import examples
chart = pyvista.ChartBox([[0, 1, 1, 2, 3, 3, 4]])
plot = chart.plot
plot.brush.texture = examples.download_puppy_texture()
chart.show()
