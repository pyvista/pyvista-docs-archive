# Display the cubemap as both an environment texture and an actor. Note that
# here we're displaying the 4k as the 16k is a bit too expensive to display
# in the documentation.
#
import pyvista as pv
from pyvista import examples
cubemap = examples.download_cubemap_space_4k()
pl = pv.Plotter(lighting=None)
_ = pl.add_actor(cubemap.to_skybox())
pl.set_environment_texture(cubemap, True)
pl.camera.zoom(0.4)
_ = pl.add_mesh(pv.Sphere(), pbr=True, roughness=0.24, metallic=1.0)
pl.show()
