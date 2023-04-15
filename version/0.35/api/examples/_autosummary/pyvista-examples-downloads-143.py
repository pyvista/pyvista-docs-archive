from pyvista import examples
cpos = [
    [-7.123e+02,  5.715e+02,  8.601e+02],
    [ 4.700e+00,  2.705e+02, -1.010e+01],
    [ 2.000e-01,  1.000e+00, -2.000e-01]
]
dataset = examples.download_urn()
dataset.plot(cpos=cpos)
