# Use a custom texture for the pie plot's brush object.
#
import pyvista
from pyvista import examples
chart = pyvista.ChartPie([4, 3, 2, 1])
plot = chart.plot
plot.brush.texture = examples.download_puppy_texture()
chart.show()
