# Create a disc with 50 points in the circumferential direction.
#
import pyvista as pv
mesh = pv.Disc(c_res=50)
mesh.plot(show_edges=True, line_width=5)
