import VMS as vms

car1 = vms.Car('Toyota', 'Supra', 1990)
car1.accelerate()
car1.brake()
# Accessing CarOptions object associated with the Car object 'car1'
co = car1.options

# Display Car details
co.CarDetails(car1.make, car1.model, car1.year)