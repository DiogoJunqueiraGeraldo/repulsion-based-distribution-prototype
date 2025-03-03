import math
import sys
import numpy as np
import random

from vector import Vector

class RepulsionBasedDistribution:
  def __init__(self, polygon, density, max_iterations):
    self.polygon = polygon
    self.density = density
    self.max_iterations = max_iterations
    
    self.points = []

    self.edges = self._calculate_edges()
    self.area = self._calculate_area()

    self.samples = math.floor(self.area * self.density)
    

  def generate_points(self):
    self.points = self._create_points()
    self.points = self._simulate_forces()

    return self.points
  
  def _closest_point_on_edge(self, edge: tuple[Vector, Vector], p: Vector):
    """Finds the closest point on edge AB to point P."""
    a, b = edge
    edge_a, edge_b, point = np.array(a), np.array(b), np.array(p)
    ab_seg = edge_b - edge_a
    ap_seg = point - edge_a

    # Projection scalar
    t = np.dot(ap_seg, ab_seg) / np.dot(ab_seg, ab_seg)

    # Clamp t to [0,1] to ensure projection remains on the segment
    t = np.clip(t, 0, 1)

    # Compute closest point
    closest_point = edge_a + t * ab_seg
    return Vector(closest_point[0].item(), closest_point[1].item())
  
  def _project_to_polygon(self, point: Vector):
    """
    Finds the closest point on a polygon's boundary to point P.
    
    :param polygon_vertices: List of (x, y) tuples defining the polygon.
    :param P: Tuple (x, y) for the external point.
    :return: Tuple (x, y) of the closest point on the polygon.
    """
    # Find the closest point among all edges
    return min((self._closest_point_on_edge(edge, point) for edge in self.edges),
               key=lambda pt: np.linalg.norm(np.array(pt) - np.array(point)))

  def _calculate_edges(self):
    polygon_vectors = [Vector(x, y) for (x, y) in self.polygon]
    edges = []
    num_vertices = len(polygon_vectors)
    
    # Use modulo to wrap around the last vertex to the first
    for i in range(num_vertices):
        a = polygon_vectors[i]
        b = polygon_vectors[(i + 1) % num_vertices]
        edges.append((a, b))
        
    return edges

  def _simulate_forces(self):
    epsilon = sys.float_info.epsilon
    k = 0.1        # Slightly reduce inter-point repulsion
    k_edge = 0.1    # Increase edge repulsion to prevent vertex sticking
    delta = 0.1     # Reduce step size for smoother movement
    tolerance = 0.001  # Reduce tolerance for finer equilibrium
    max_force_magnitude = 0.1  # Maximum allowable force magnitude
    
    points = [Vector(x, y) for (x, y) in self.points]
    
    for iteration in range(self.max_iterations):
      max_move = 0
      new_points = []
      for i, p in enumerate(points):
        net_force = Vector(0, 0)

        # Repulsive force from other points
        for j, q in enumerate(points):
          if i == j: continue
          r =  p - q
          distance = max(r.magnitude(), epsilon)  # avoid division by zero
          net_force += (k * r.normalized()) / ((distance)**2)
      
        # Repulsive force from each edge
        for edge in self.edges:
          q = self._closest_point_on_edge(edge, p)
          r_edge = p - q
          distance_edge = max(r_edge.magnitude(), epsilon)
          net_force += (k_edge * r_edge.normalized()) / ((distance_edge)**3)
        

        net_force = net_force.clamp(max_force_magnitude)  # Apply force clamping

        # Update position
        p_new = p + delta * net_force
        
        # Project back into polygon if necessary
        if not self._is_point_inside(p_new):
          p_new = self._project_to_polygon(p_new)
        
        new_points.append(p_new)
        max_move = max(max_move, (p_new - p).magnitude())
    
      points = new_points
      print(f"Iteration {iteration} max mov {max_move}")
      if max_move < tolerance:
          print(f"It found equilibrium within the {iteration} iteration")
          break
    
    return [(x.x, x.y) for x in points]


  def _create_points(self):
    """Create points uniformly through the polygon"""
    points = []
    while len(points) < self.samples:
        x = random.uniform(min(p[0] for p in self.polygon), max(p[0] for p in self.polygon))
        y = random.uniform(min(p[1] for p in self.polygon), max(p[1] for p in self.polygon))
        if self._is_point_inside((x, y)):
            points.append((x, y))

    return points

  def _calculate_area(self):
    """Shoelace formula for polygon area"""
    n = len(self.polygon)
    area = 0
    for i in range(n):
      x1, y1 = self.polygon[i]
      x2, y2 = self.polygon[(i + 1) % n]
      area += x1 * y2 - x2 * y1
    return abs(area) / 2

  
  def _distance_to(self, p1, p2):
    """Hypothenusa to calculate distance"""
    (p1_x, p1_y) = p1
    (p2_x, p2_y) = p2

    return math.hypot(p1_x - p2_x, p1_y - p2_y)

  def _is_point_inside(self, point):
    """Ray casting algorithm to check polygon containment"""
    x, y = point
    inside = False
    n = len(self.polygon)

    for i in range(n):
        p1 = self.polygon[i]
        p2 = self.polygon[(i+1) % n]
        
        # Check if point crosses polygon edge
        if ((p1[1] > y) != (p2[1] > y)):
            x_intersect = (y - p1[1]) * (p2[0] - p1[0]) / (p2[1] - p1[1]) + p1[0]
            if x <= x_intersect:
                inside = not inside
    return inside