class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def __str__(self):
        return f"Your car model is {self.brand} - {self.model}, color is {self.color}"
