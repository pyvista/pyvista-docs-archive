# Set the x-axis tick label font size of a 2D chart to 20.
#
import pyvista
chart = pyvista.Chart2D()
_ = chart.line([0, 1, 2], [2, 1, 3])
chart.x_axis.tick_label_size = 20
chart.x_axis.tick_label_size
# Expected:
## 20
chart.show()
