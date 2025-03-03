import math
import numpy as np

class Vector:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def clamp(self, max_magnitude):
        # Calculate the magnitude of the vector
        mag = self.magnitude()
        if mag > max_magnitude:
            # If the magnitude is greater than max_magnitude, normalize and scale the vector
            return self.normalized() * max_magnitude
        return self
    
    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    def normalized(self):
        m = self.magnitude()
        if m == 0:
            return Vector(0, 0)  # To avoid division by zero
        return Vector(self.x / m, self.y / m)

    def __array__(self, dtype=None):
      return np.array([self.x, self.y], dtype=dtype)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __rmul__(self, scalar):
          return self.__mul__(scalar)
    
    def __iter__(self):
        # This allows for tuple unpacking: (x, y) = vector_instance
        yield self.x
        yield self.y

    def __truediv__(self, scalar):
        return Vector(self.x / scalar, self.y / scalar)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
