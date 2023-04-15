import pyvista
from pyvista import examples
filename = examples.download_mars_jpg()
filename.split("/")[-1]  # omit the path
# Expected:
## 'mars.jpg'
reader = pyvista.get_reader(filename)
mesh = reader.read()
mesh.plot()
