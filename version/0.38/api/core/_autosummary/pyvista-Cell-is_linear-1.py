import pyvista
mesh = pyvista.Sphere()
mesh.cell[0].is_linear
# Expected:
## True
