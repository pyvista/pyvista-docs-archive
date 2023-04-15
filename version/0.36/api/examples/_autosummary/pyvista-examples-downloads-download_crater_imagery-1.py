from pyvista import examples
cpos = [
    [  66.,  73. , -382.6],
    [  66.,  73. ,    0. ],
    [  -0.,  -1. ,    0. ]
]
dataset = examples.download_crater_imagery()
dataset.plot(cpos=cpos)
