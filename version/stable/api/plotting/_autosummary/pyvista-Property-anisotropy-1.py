# Set anisotropy to 0.1
#
import pyvista as pv
prop = pv.Property()
prop.interpolation = 'pbr'  # requires physically based rendering
prop.anisotropy
# Expected:
## 0.1
