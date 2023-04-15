import pyvista
superquadric = pyvista.Superquadric(scale=(3., 1., 0.5),
                                    phi_roundness=0.1,
                                    theta_roundness=0.5)
superquadric.plot(show_edges=True)
