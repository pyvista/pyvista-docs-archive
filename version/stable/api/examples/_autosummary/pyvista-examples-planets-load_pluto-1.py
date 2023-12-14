import pyvista as pv
from pyvista import examples
mesh = examples.planets.load_pluto()
texture = examples.planets.download_pluto_surface(texture=True)
pl = pv.Plotter()
image_path = examples.planets.download_stars_sky_background(
    load=False
)
pl.add_background_image(image_path)
_ = pl.add_mesh(mesh, texture=texture)
pl.show()
