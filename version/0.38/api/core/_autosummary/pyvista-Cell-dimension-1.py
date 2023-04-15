import pyvista
mesh = pyvista.Sphere()
mesh.cell[0].dimension
# Expected:
## 2
