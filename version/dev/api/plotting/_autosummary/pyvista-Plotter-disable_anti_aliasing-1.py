import pyvista
pl = pyvista.Plotter()
pl.disable_anti_aliasing()
_ = pl.add_mesh(pyvista.Sphere(), show_edges=True)
pl.show()
#
# See :ref:`anti_aliasing_example` for a full example demonstrating
