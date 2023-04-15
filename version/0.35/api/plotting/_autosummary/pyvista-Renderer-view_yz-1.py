# View the YZ plane of a built-in mesh example.
#
from pyvista import examples
import pyvista as pv
airplane = examples.load_airplane()
pl = pv.Plotter()
_ = pl.add_mesh(airplane)
pl.view_yz()
pl.show()
