# INSTRUCTION: Do what is asked in each item below.

1. Answer the following questions: 


a. What is duck typing, as explained in the video?

   Duck typing is a method used to achieve polymorphism, without using inheritance. Given that objects that resemble one another have the minimum necessary similar properties and/or methods. Basically, "If it looks like a duck and quacks like a a duck, it must be a duck." Which is basically saying that if objects have the same attributes as a duck ("if it looks like a duck")  and have the same methods ("if it quacks like a duck") then they are objects of the same class.


b. What did the Car class need to have so it could work inside the same loop as Dog and  Cat, even if it does not inherit from the Animal class? 

   It needed the same method as them, which was the method of speaking. Since before that, it had the method horn. Meanwhile, the rest of the objects (the actual animals) had speak methods. 


2. Create the Python code that:

a. Creates three classes: Car, Boat, and Drone with a method move().
move() in the Car class prints "The car drives on the road."
move() in the Boat class prints "The boat sails on water."
move() in the Drone class prints "The drone flies in the sky."


b. Has a function named start_trip(vehicle), with a parameter vehicle, that simply calls the move() method: vehicle.move().


c. Creates one object of each class. 


d. Calls the start_trip() method for each object.


[CODE](sg11_Polymorphism_Activity2.py)


3. How does the code in 2.2 demonstrate polymorphism?

   It demostrates polyphormism because there are multiple vechiles that take different forms like a car, boat, and drone.
