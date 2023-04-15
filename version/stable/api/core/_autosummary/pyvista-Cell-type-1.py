import pyvista
mesh = pyvista.Sphere()
mesh.cell[0].type
# Expected:
## <CellType.TRIANGLE: 5>
