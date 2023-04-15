# Create a sphere and translate it by ``(2, 1, 2)``.
#
import pyvista
mesh = pyvista.Sphere()
mesh.center
# Expected:
## [0.0, 0.0, 0.0]
trans = mesh.translate((2, 1, 2), inplace=True)
trans.center
# Expected:
## [2.0, 1.0, 2.0]
