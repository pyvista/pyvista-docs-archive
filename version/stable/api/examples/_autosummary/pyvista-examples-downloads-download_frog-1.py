from pyvista import examples
cpos = [
    [ 8.4287e+02, -5.7418e+02, -4.4085e+02],
    [ 2.4950e+02,  2.3450e+02,  1.0125e+02],
    [-3.2000e-01,  3.5000e-01, -8.8000e-01]
]
dataset = examples.download_frog()
dataset.plot(volume=True, cpos=cpos)
#
# See :ref:`volume_rendering_example` for an example using
