# ------------------------------
# Factory Design Pattern Example
# ------------------------------

# Step 1: Define a common interface (or abstract class)
class Shape:
    def draw(self):
        # This method will be implemented by each specific shape
        pass


# Step 2: Create concrete classes that implement the interface
class Circle(Shape):
    def draw(self):
        print("Drawing Circle")


class Square(Shape):
    def draw(self):
        print("Drawing Square")


# Step 3: Create the Factory Class
# This class decides which object (Circle or Square) to create
class ShapeFactory:
    def get_shape(self, shape_type):
        if shape_type == "circle":
            # Factory creates and returns a Circle object
            return Circle()
        elif shape_type == "square":
            # Factory creates and returns a Square object
            return Square()
        else:
            # If the type is unknown, return None
            return None


# Step 4: Client Code
# The client asks the factory for the object it needs
factory = ShapeFactory()                # Create the factory object

shape = factory.get_shape("circle")     # Ask factory to give a Circle object
shape.draw()                            # Use the returned object












#  Without Factory Pattern

# The client code must know which class to use.
# This creates tight coupling and duplication.

# shape_type = "circle"

# if shape_type == "circle":
#     shape = Circle()
# elif shape_type == "square":
#     shape = Square()
# else:
#     shape = None

# if shape:
#     shape.draw()
