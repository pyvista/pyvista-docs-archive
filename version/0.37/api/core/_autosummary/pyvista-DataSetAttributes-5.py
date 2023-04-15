# Add two arrays to the mesh point data.
#
import pyvista
mesh = pyvista.Sphere()
mesh.point_data['my_data'] = range(mesh.n_points)
mesh.point_data['my_other_data'] = range(mesh.n_points)
mesh.point_data.active_scalars_name
# Expected:
## 'my_other_data'
#
# Set the name of the active scalars.
#
mesh.point_data.active_scalars_name = 'my_data'
mesh.point_data.active_scalars_name
# Expected:
## 'my_data'
