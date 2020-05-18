# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed .

class GroundVehicle():
    #Default wheels must be 4
    def __init__(self, num_wheels=4):
        self.num_wheels = num_wheels
    #method added
    def drive(self):
        return "vroooom"

    # TODO

# Subclass Motorcycle from GroundVehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it returns "BRAAAP!!"

# TODO

class Motorcycle(GroundVehicle):
    def __init__(self, number_of_wheels=2):
        #used for multi-level inheritance
        super().__init__(number_of_wheels)

    #overriding drive method
    def drive(self):
        return "BRAAAP!!"

vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]

# Go through the vehicles list and print the result of calling drive() on each.
#Need a loop to map over the list
for v in vehicles:
    print(v.drive())
# TODO

