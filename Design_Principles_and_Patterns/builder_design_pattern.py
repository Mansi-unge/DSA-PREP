# -------------------------------
# Builder Design Pattern Example
# -------------------------------

# The complex object we want to build
class Computer:
    def __init__(self):
        self.cpu = None
        self.gpu = None
        self.ram = None


# The Builder class that helps us construct a Computer step by step
class ComputerBuilder:
    def __init__(self):
        # Start with an empty Computer object
        self.computer = Computer()

    def set_cpu(self, cpu):
        self.computer.cpu = cpu
        return self  # returning self allows method chaining

    def set_gpu(self, gpu):
        self.computer.gpu = gpu
        return self

    def set_ram(self, ram):
        self.computer.ram = ram
        return self

    def build(self):
        # Return the fully constructed Computer object
        return self.computer


# Client Code
# Construct the computer step-by-step (chained calls)
pc = (
    ComputerBuilder()
    .set_cpu("Intel i7")
    .set_gpu("RTX 4080")
    .set_ram("32GB")
    .build()
)

# Display the final Computer configuration
print(pc.__dict__)
