import pyvista as pv
from pyvista import examples
filename = examples.download_teapot(load=False)
filename.split("/")[-1]  # omit the path
# Expected:
## 'teapot.g'
reader = pv.get_reader(filename)
mesh = reader.read()
mesh.plot(cpos='xy', show_scalar_bar=False)
