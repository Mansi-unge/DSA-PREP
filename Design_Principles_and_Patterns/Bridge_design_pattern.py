# --------------------------------------------
# Bridge Design Pattern Example
# --------------------------------------------

# Implementation Layer (the "how")
# The base interface for all drawing APIs
class DrawingAPI:
    def draw_circle(self, x, y, radius):
        pass


# Concrete Implementations
class DrawingAPI1(DrawingAPI):
    def draw_circle(self, x, y, radius):
        print(f"API1: Drawing circle at ({x}, {y}) with radius {radius}")


class DrawingAPI2(DrawingAPI):
    def draw_circle(self, x, y, radius):
        print(f"API2: Drawing circle at ({x}, {y}) with radius {radius}")


# Abstraction Layer (the "what")
# Circle uses a DrawingAPI object to actually draw itself
class Circle:
    def __init__(self, x, y, radius, drawing_api):
        self.x = x
        self.y = y
        self.radius = radius
        self.drawing_api = drawing_api  # Bridge to the implementation layer

    def draw(self):
        # Delegate the drawing operation to the chosen DrawingAPI
        self.drawing_api.draw_circle(self.x, self.y, self.radius)


# Client Code
circle1 = Circle(1, 2, 3, DrawingAPI1())  # Use DrawingAPI1
circle2 = Circle(5, 7, 11, DrawingAPI2()) # Use DrawingAPI2

circle1.draw()
circle2.draw()
