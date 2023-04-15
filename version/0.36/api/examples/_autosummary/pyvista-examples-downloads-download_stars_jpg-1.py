from pyvista import examples
import pyvista as pv
pl = pv.Plotter()
dataset = examples.download_stars_jpg()
pl.add_background_image(dataset)
pl.show()
