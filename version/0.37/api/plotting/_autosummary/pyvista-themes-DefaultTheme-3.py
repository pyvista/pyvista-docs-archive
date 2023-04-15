# Use super-sampling anti-aliasing in the global theme.
#
import pyvista
pyvista.global_theme.anti_aliasing = 'ssaa'
pyvista.global_theme.anti_aliasing
# Expected:
## 'ssaa'
#
# Disable anti-aliasing in the global theme.
#
import pyvista
pyvista.global_theme.anti_aliasing = None
#
# See :ref:`anti_aliasing_example` for more information regarding
