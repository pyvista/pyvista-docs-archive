from pyvista import examples
mesh = examples.load_hexbeam()
cell = mesh.cell[0]
cell.plot()
