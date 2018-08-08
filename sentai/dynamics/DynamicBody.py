from sentai.vectors.Vector3 import Vector3


class DynamicBody:

    def __init__(self, position: Vector3, velocity: Vector3, mass):
        self.position = position
        self.velocity = velocity
        self.mass = mass

    def momentum(self):
        return self.velocity * self.mass


class CollidingBody(DynamicBody):

    def __init__(self, position, velocity, mass, radius):
        DynamicBody.__init__(self, position, velocity, mass)
        self.radius = radius