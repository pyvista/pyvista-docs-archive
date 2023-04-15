import pyvista
mesh = pyvista.Sphere()
mesh.cell[0].n_points
# Expected:
## 3
