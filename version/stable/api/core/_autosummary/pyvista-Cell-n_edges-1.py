import pyvista
mesh = pyvista.Sphere()
mesh.cell[0].n_edges
# Expected:
## 3
