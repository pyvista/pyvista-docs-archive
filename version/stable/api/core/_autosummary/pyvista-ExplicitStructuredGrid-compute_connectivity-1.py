from pyvista import examples
grid = examples.load_explicit_structured()
grid = grid.compute_connectivity()
grid.plot(show_edges=True)
