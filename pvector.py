import math

class PVector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, pvector):
        self.x += pvector.x
        self.y += pvector.y

    def __add__(self, rhs):
        return PVector(self.x + rhs.x, self.y + rhs.y)

    def sub(self, pvector):
        self.x -= pvector.x
        self.y -= pvector.y

    def __sub__(self, rhs):
        return PVector(self.x - rhs.x, self.y - rhs.y)

    def mult(self, n):
        self.x *= n
        self.y *= n

    def div(self, n):
        self.x /= n
        self.y /= n

    def get(self):
        return PVector(self.x, self.y)

    def mag(self):
        return math.sqrt(self.x**2 + self.y**2)

    def normalize(self):
        m = self.mag()
        if m != 0:
            self.div(m)

    def distance(self, p):
        return math.sqrt(((self.x - p.x)**2) + ((self.y - p.y)**2))

    def limit(self, max):
        if self.mag() > max:
            self.normalize()
            self.mult(max)

