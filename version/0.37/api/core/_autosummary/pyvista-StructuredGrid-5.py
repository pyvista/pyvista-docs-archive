import pyvista
import numpy as np
xrng = np.arange(-10, 10, 1, dtype=np.float32)
yrng = np.arange(-10, 10, 2, dtype=np.float32)
zrng = np.arange(-10, 10, 5, dtype=np.float32)
x, y, z = np.meshgrid(xrng, yrng, zrng)
grid = pyvista.StructuredGrid(x, y, z)
grid.x.shape
# Expected:
## (10, 20, 4)
