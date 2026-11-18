class Patient: # Creates the class "Patient" 
  def __init__(self, name: str, bill_amount: int): # Creates the properties of the Patient class in which this case its name, which is a string, and the bill_amount, which is an integer.
    self._name = name 
    self._bill_amount = bill_amount 

  def get_name(self): # Defines the method, get_name, which when called will print the name of the patient
    return self._name
  def set_name(self, name): # Defines the method, set_name, which when used can replace the name originally given with a new one.
    self._name = name 

  def get_bill_amount(self): # Defines the method, get_bill_amount, which when called will print the bill amount of the patient
    return self._bill_amount 
  def set_bill_amount(self, bill_amount): # Defines the method, set_bill_amount, which when used can replace the bill amount originally given with a new one.
    self._bill_amount = bill_amount 

  def calculate_bill(self): # Normally simply returns the bill amount, like the method: get_bill_amount, but this will play great importance later where I used this method as a place where I put discounts for the Senior Citizen and PhilHealth patients 
    return self._bill_amount

  def display_patient_type(self): # Prints: "Patient Type: Regular Patient" when called 
    print("Patient Type: Regular Patient")

class SeniorPatient(Patient): # Creates the childclass of Patient, which is SeniorPatient.
  def __init__(self, name: str, bill_amount: int):
    super().__init__(name, bill_amount) # Super initializes the name and bill amount from parent class so we dont have to define them here.

  def calculate_bill(self): # Does the operation of the 20% discount for senior citizens and returns it to bill_amount
    self._bill_amount = self._bill_amount - 0.2*self._bill_amount
    return self._bill_amount

  def display_patient_type(self):
    print("Patient Type: Senior Citizen")

class PhilHealthPatient(Patient): # Creates another childclass of Patient, which is PhilHealthPatient
  def __init__(self, name: str, bill_amount: int):
    super().__init__(name, bill_amount) # Super initializes the name and bill amount from parent class so we dont have to define them here.

  def calculate_bill(self): # Does the operation of the 15% discount for senior citizens and returns it to bill_amount
    self._bill_amount = self._bill_amount - 0.15*self._bill_amount 
    return self._bill_amount 
    
  def display_patient_type(self):
    print("Patient Type: PhilHealth Member")

print("Hospital Billing System")
print("-----------------------")

p1 = Patient("Juan Dela Cruz", 15000.00) # Creates an object from the Patient Class
print(f"Patient Name: {p1.get_name()}") # Calls the name of p1, which is Juan Dela Cruz
p1.display_patient_type()
print(f"Original Bill: ₱{p1.get_bill_amount():,.2f}") # The :,.2f does two things. The comma is used so that when it is printed it puts a comma to signify that its in the thousands and the .2f is so that it outputs with two decimal places instead of 1
print(f"Final Bill: ₱{p1.calculate_bill():,.2f}")# Same as above

print()

p2 = SeniorPatient("Maria Santos", 15000.00)
print(f"Patient Name: {p2.get_name()}")
p2.display_patient_type()
print(f"Original Bill: ₱{p2.get_bill_amount():,.2f}") # Same as above
print(f"Final Bill: ₱{p2.calculate_bill():,.2f}")

print()

p3 = PhilHealthPatient("Pedro Reyes", 15000.00)
print(f"Patient Name: {p3.get_name()}")
p3.display_patient_type()
print(f"Original Bill: ₱{p3.get_bill_amount():,.2f}") # Same as above
print(f"Final Bill: ₱{p3.calculate_bill():,.2f}")





