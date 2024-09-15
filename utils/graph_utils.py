import numpy as np
import networkx as nx
from scipy.spatial import Delaunay
from .irrigation_utils import is_edge_valid

def process_image(image_array, ditch_threshold):
    """Generate random points avoiding dark areas."""
    height, width = image_array.shape
    num_points = 200
    points = []

    while len(points) < num_points:
        x = np.random.randint(0, width)
        y = np.random.randint(0, height)
        if image_array[y, x] > ditch_threshold:
            points.append([x, y])

    return np.array(points)

def generate_graph(points, image_array, ditch_threshold):
    """Perform Delaunay triangulation and generate the graph."""
    tri = Delaunay(points)
    G = nx.Graph()

    for simplex in tri.simplices:
        for i in range(3):
            p1 = tuple(points[simplex[i]])
            p2 = tuple(points[simplex[(i + 1) % 3]])
            if is_edge_valid(p1, p2, image_array, ditch_threshold):
                G.add_edge(p1, p2, weight=np.linalg.norm(np.array(p1) - np.array(p2)))
    
    return tri, G

def ensure_connected(G):
    """Ensure the graph is connected by adding edges."""
    if not nx.is_connected(G):
        # Compute the Minimum Spanning Tree of the graph
        mst = nx.minimum_spanning_tree(G)
        return mst
    return G
