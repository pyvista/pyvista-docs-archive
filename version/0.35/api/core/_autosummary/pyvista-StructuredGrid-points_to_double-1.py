# Create a mesh that has points of the type ``float32`` and
# convert the points to ``float64``.
#
import pyvista
mesh = pyvista.Sphere()
mesh.points.dtype
# Expected:
## dtype('float32')
_ = mesh.points_to_double()
mesh.points.dtype
# Expected:
## dtype('float64')
