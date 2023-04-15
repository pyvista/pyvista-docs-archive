"""
Walk through version/stable and generate redirects in the root of this
directory. This will allow a stable transition between original content at

https://docs.pyvista.org/

to

https://docs.pyvista.org/version/stable/

This probably only needs to happen once during the initial transition.

"""
import os
import shutil


TEMPLATE = """<!DOCTYPE html>
<meta charset="utf-8">
<title>Redirecting to https://docs.pyvista.org/%s</title>
<meta http-equiv="refresh" content="0; URL=/%s">
<link rel="canonical" href="https://docs.pyvista.org/%s">
"""

def create_redirect(path):
    redirect_path = os.path.relpath(path, start="version/stable")
    redirect_content = TEMPLATE % (path, path, path)

    target_dir = os.path.dirname(redirect_path)
    if target_dir:
        os.makedirs(target_dir, exist_ok=True)
    
    with open(redirect_path, "w") as f:
        f.write(redirect_content)

for root, dirs, files in os.walk("version/stable"):
    for file in files:
        if file.endswith(".html"):
            full_path = os.path.join(root, file)
            create_redirect(full_path)
