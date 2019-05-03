# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
class Vehicle(): # Base Vehicle Class
    def __init__(self):
        super().__init__()
    pass

class  FlightVehicle(Vehicle): # Flight Vehicle
    def __init__(self):
        super().__init__()
    pass

class Starship(FlightVehicle): # Starship
    def __init__(self):
        super().__init__()
    pass

class Airplane(FlightVehicle): # Airplane
    def __init__(self):
        super().__init__()
    pass

class GroundVehicle(Vehicle): # Ground Vehicle
    def __init__(self):
        super().__init__()
    pass

class Car(GroundVehicle): # Car
    def __init__(self):
        super().__init__()
    pass

class Motorcycle(GroundVehicle): # Motorcycle
    def __init__(self):
        super().__init__()
    pass
    
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class
