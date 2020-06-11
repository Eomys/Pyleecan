# -*- coding: utf-8 -*-

import pyvistaqt as pv


def plot_mesh(self, indices=[]):
    """Plot the mesh using pyvista plotter.

    Parameters
    ----------
    self : MeshFile
        a MeshFile object
    indices : list
        list of the points to extract (optional)

    Returns
    -------
    """

    mesh = self.get_mesh(indices)

    # Configure plot
    p = pv.Plotter()
    p.add_mesh(
        mesh,
        color="grey",
        opacity=1,
        show_edges=True,
        edge_color="white",
        line_width=1,
    )
    p.show()