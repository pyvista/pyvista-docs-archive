import pyvista
import vtk
import numpy as np
#
# Create an empty structured grid.
#
grid = pyvista.StructuredGrid()
#
# Initialize from a ``vtk.vtkStructuredGrid`` object
#
vtkgrid = vtk.vtkStructuredGrid()
grid = pyvista.StructuredGrid(vtkgrid)
#
# Create from NumPy arrays.
#
xrng = np.arange(-10, 10, 2, dtype=np.float32)
yrng = np.arange(-10, 10, 2, dtype=np.float32)
zrng = np.arange(-10, 10, 2, dtype=np.float32)
x, y, z = np.meshgrid(xrng, yrng, zrng)
grid = pyvista.StructuredGrid(x, y, z)
grid  # doctest:+SKIP
# Expected:
## StructuredGrid (0x7fb18f2a8580)
## N Cells:    729
## N Points:   1000
## X Bounds:   -1.000e+01, 8.000e+00
## Y Bounds:   -1.000e+01, 8.000e+00
## Z Bounds:   -1.000e+01, 8.000e+00
## Dimensions: 10, 10, 10
## N Arrays:   0
