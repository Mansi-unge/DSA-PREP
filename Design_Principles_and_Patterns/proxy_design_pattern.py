# ------------------------------------------
# Proxy Design Pattern Example
# ------------------------------------------

# Real Object (the heavy or sensitive one)
class RealImage:
    def __init__(self, filename):
        self.filename = filename
        self.load_image()  # simulate heavy loading

    def load_image(self):
        # Simulating a time-consuming operation
        print(f"Loading image from {self.filename}")

    def display(self):
        print(f"Displaying {self.filename}")


# Proxy Object (controls access to the real one)
class ProxyImage:
    def __init__(self, filename):
        self.filename = filename
        self.real_image = None  # Real object not created yet (lazy loading)

    def display(self):
        # Create the real object only when needed
        if self.real_image is None:
            self.real_image = RealImage(self.filename)
        # Forward the request to the real object
        self.real_image.display()


# Client Code
image = ProxyImage("photo.png")

# Image is not loaded yet — proxy controls access
image.display()  # First time: loads and displays
image.display()  # Second time: directly displays (no reloading)
