# Get the last cell of a dataset.
#
from pyvista import examples
mesh = examples.load_hexbeam()
mesh.cell[-1] # doctest:+SKIP
# Expected:
## Type: CellType.HEXAHEDRON
## Linear: True
## Dimension: 3
## N Points: 8
## N Faces: 6
## N Edges: 12
## X Bounds: 5.000e-01, 1.000e+00
## Y Bounds: 5.000e-01, 1.000e+00
## Z Bounds: 4.500e+00, 5.000e+00
#
# Get the point ids of the last cell
#
mesh.cell[-1].point_ids
# Expected:
## [98, 62, 53, 80, 17, 13, 12, 15]
#
# Get the points coordinates of the last cell
#
mesh.cell[-1].points
# Expected:
## array([[0.5, 0.5, 4.5],
##        [1. , 0.5, 4.5],
##        [1. , 1. , 4.5],
##        [0.5, 1. , 4.5],
##        [0.5, 0.5, 5. ],
##        [1. , 0.5, 5. ],
##        [1. , 1. , 5. ],
##        [0.5, 1. , 5. ]])
#
# Get the point ids of the edges of the last cell.
# Note that the `edges` attributes returns a generator of
# `pyvista.Cell` objects.
#
for e in mesh.cell[-1].edges:
    print(e.point_ids)
# Expected:
## [98, 62]
## [62, 53]
## [80, 53]
## [98, 80]
## [17, 13]
## [13, 12]
## [15, 12]
## [17, 15]
## [98, 17]
## [62, 13]
## [80, 15]
## [53, 12]
#
# Get the point ids of the faces of the last cell.
#
from pyvista.examples.cells import Tetrahedron
mesh = Tetrahedron()
cell = mesh.cell[-1]
for face in cell.faces:
    print(face.point_ids)
# Expected:
## [0, 1, 3]
## [1, 2, 3]
## [2, 0, 3]
## [0, 2, 1]
