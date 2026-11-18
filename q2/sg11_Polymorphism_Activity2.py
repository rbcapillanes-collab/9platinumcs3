class Car: # Creates the car class and its method is move which prints "The car drives on the road."
    def move(self):
        print("The car drives on the road.")

class Boat: # Creates the boat class and it has the same method as the car one, but with a different print 
    def move(self):
        print("The boat sails on water.")

class Drone: # Creates the drone class and it has the same method as the ones above but again with a different print
    def move(self):
        print("The drone flies in the sky.")

vehicles = [Car(), Boat(), Drone()] # Creates a list of objects 

def start_trip(vehicle): # Creates function in which checks if the vehicles above have a move method.
    vehicle.move()

for vehicle in vehicles: # If the objects pass the start trip function, then it moves onto here where their moves get printed.
  start_trip(vehicle)

