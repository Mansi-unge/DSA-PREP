# ---------------------------------------
# Adapter Design Pattern Example
# ---------------------------------------

# Target Interface (what the client expects)
class EuropeanSocket:
    def supply_220v(self):
        return "220V"


# Adaptee (the existing class with a different interface)
class USASocket:
    def supply_110v(self):
        return "110V"


# Adapter (makes USA socket compatible with European socket)
class Adapter:
    def __init__(self, usa_socket):
        # Take the USA socket object and adapt it
        self.usa_socket = usa_socket

    def supply_220v(self):
        # Convert (adapt) 110V to 220V
        return self.usa_socket.supply_110v() + " adapted to 220V"


# Client Code (wants 220V power)
usa_socket = USASocket()          # Existing incompatible class
adapter = Adapter(usa_socket)     # Use adapter to make it compatible

# Now the client gets 220V output (through adaptation)
print(adapter.supply_220v())
