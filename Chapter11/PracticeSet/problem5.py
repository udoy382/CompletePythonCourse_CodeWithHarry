class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        # Correctly create a new Vector by adding corresponding components
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __mul__(self, other):
        # Return the dot product of the two vectors
        return self.x * other.x + self.y * other.y + self.z * other.z

    def __str__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"
    
# Test the implementation
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v3 = Vector(7, 8, 9) # Same dimension vector

print(v2 + v2) # Output: Vector(8, 10, 12)
print(v2 * v2) # Output: 77

print(v1 + v3) # Output: Vector(8, 10, 12)
print(v1 * v3) # Output: 50
