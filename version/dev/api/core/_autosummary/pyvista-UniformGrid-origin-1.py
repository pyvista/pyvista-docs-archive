import pyvista
grid = pyvista.UniformGrid(dimensions=(5, 5, 5))
grid.origin
# Expected:
## (0.0, 0.0, 0.0)
#
# Show how the origin is in the bottom "southwest" corner of the
# UniformGrid.
#
pl = pyvista.Plotter()
_ = pl.add_mesh(grid, show_edges=True)
_ = pl.add_axes_at_origin(ylabel=None)
pl.camera_position = 'xz'
pl.show()
#
# Set the origin to ``(1, 1, 1)`` and show how this shifts the
# UniformGrid.
#
grid.origin = (1, 1, 1)
pl = pyvista.Plotter()
_ = pl.add_mesh(grid, show_edges=True)
_ = pl.add_axes_at_origin(ylabel=None)
pl.camera_position = 'xz'
pl.show()
