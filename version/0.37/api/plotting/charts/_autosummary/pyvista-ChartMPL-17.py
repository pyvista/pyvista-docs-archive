# Create a matplotlib chart.
#
import pyvista
chart = pyvista.ChartMPL()
plots = chart.figure.axes[0].plot([0, 1, 2], [2, 1, 3])
chart.show()
#
# Hide it.
#
chart.toggle()
chart.show()
