import pyvista
grid = pyvista.UniformGrid(dims=(2, 2, 2))
grid.points
# Expected:
## array([[0., 0., 0.],
##        [1., 0., 0.],
##        [0., 1., 0.],
##        [1., 1., 0.],
##        [0., 0., 1.],
##        [1., 0., 1.],
##        [0., 1., 1.],
##        [1., 1., 1.]])
