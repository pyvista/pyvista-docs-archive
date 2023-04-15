import pyvista
mesh = pyvista.Sphere()
pointset = mesh.cast_to_pointset()
type(pointset)
# Expected:
## <class 'pyvista.core.pointset.PointSet'>
