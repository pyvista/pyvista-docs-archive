# Create a multiple lines between ``(0, 0, 0)``, ``(1, 1, 1)`` and ``(0, 0, 1)``.
#
import pyvista as pv
mesh = pv.MultipleLines(points=[[0, 0, 0], [1, 1, 1], [0, 0, 1]])
plotter = pv.Plotter()
actor = plotter.add_mesh(mesh, color='k', line_width=10)
plotter.camera.azimuth = 45
plotter.camera.zoom(0.8)
plotter.show()
