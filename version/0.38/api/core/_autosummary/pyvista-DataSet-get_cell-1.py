# Get the 0-th cell.
#
from pyvista import examples
mesh = examples.load_airplane()
mesh.get_cell(0) # doctest:+SKIP
# Expected:
## GenericCell (0x7f6304e0a730)
##   Type: CellType.TRIANGLE
##   Linear:       True
##   Dimension:    2
##   N Points:     3
##   N Faces:      0
##   N Edges:      3
##   X Bounds:     8.970e+02, 9.075e+02
##   Y Bounds:     4.876e+01, 5.549e+01
##   Z Bounds:     8.075e+01, 8.366e+01
