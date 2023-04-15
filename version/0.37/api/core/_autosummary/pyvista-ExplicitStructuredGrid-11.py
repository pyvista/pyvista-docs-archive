from pyvista import examples
grid = examples.load_explicit_structured()
grid = grid.hide_cells(range(80, 120))
grid.plot(color='w', show_edges=True, show_bounds=True)
#
grid = grid.show_cells()
grid.plot(color='w', show_edges=True, show_bounds=True)
