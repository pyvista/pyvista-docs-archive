# Create a blue color with half opacity.
#
import pyvista
c = pyvista.Color("blue", default_opacity="#80")
c
# Expected:
## Color(name='blue', hex='#0000ff80')
c.hex_rgba
# Expected:
## '#0000ff80'
#
# Create a transparent red color using an RGBA hexadecimal value.
#
c = pyvista.Color("0xff000040")
c
# Expected:
## Color(name='red', hex='#ff000040')
c.hex_rgba
# Expected:
## '#ff000040'
