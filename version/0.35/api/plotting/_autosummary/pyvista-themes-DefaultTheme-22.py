# Enable the pythreejs backend.
#
import pyvista as pv
pv.set_jupyter_backend('pythreejs')
#
# Enable the ipygany backend.
#
import pyvista as pv
pv.set_jupyter_backend('ipygany')
#
# Enable the panel backend.
#
pv.set_jupyter_backend('panel')
#
# Enable the ipyvtklink backend.
#
pv.set_jupyter_backend('ipyvtklink')
#
# Just show static images.
#
pv.set_jupyter_backend('static')
#
# Disable all plotting within JupyterLab and display using a
# standard desktop VTK render window.
#
pv.set_jupyter_backend(None)  # or 'none'
