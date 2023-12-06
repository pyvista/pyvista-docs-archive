import pyvista as pv
from pyvista import examples
filename = examples.download_gif_simple(load=False)
filename.split("/")[-1]  # omit the path
# Expected:
## 'sample.gif'
reader = pv.get_reader(filename)
mesh = reader.read()
mesh.plot(rgba=True, zoom='tight', border=True, border_width=2)
