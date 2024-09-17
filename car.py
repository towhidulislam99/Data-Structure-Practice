class Car:
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.fuel_level = 0  # Initial fuel level

    def get_fuel_level(self):
        """Return the car's current fuel level."""
        return self.fuel_level

    def fill_tank(self):
        """Fill the car's tank."""
        self.fuel_level = 100
        print(f"Tank is now full.")

    def __str__(self):
        """Return a neatly formatted descriptive name."""
        return f"{self.year} {self.make} {self.model}, Fuel level: {self.fuel_level}"
