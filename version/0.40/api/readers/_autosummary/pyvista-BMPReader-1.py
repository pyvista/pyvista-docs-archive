import pyvista
from pyvista import examples
filename = examples.download_masonry_texture(load=False)
filename.split("/")[-1]  # omit the path
# Expected:
## 'masonry.bmp'
reader = pyvista.get_reader(filename)
mesh = reader.read()
mesh.plot()
