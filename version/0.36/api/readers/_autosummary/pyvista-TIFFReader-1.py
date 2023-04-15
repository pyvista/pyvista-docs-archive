import pyvista
from pyvista import examples
filename = examples.download_crater_imagery(load=False)
filename.split("/")[-1]  # omit the path
# Expected:
## 'BJ34_GeoTifv1-04_crater_clip.tif'
reader = pyvista.get_reader(filename)
mesh = reader.read()
mesh.plot()
