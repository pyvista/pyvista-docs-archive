from pyvista import examples
mesh = examples.load_hexbeam()
mesh.cell_bounds(0)
# Expected:
## (0.0, 0.5, 0.0, 0.5, 0.0, 0.5)
mesh.point_is_inside_cell(0, [0.2, 0.2, 0.2])
# Expected:
## True
