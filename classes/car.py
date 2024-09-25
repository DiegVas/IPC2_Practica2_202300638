class Car:
    def __init__(self, Placa, brand, model, description, unit_price, quantity, image):
        self.Placa = Placa  # Integer that identifies a type of car
        self.brand = brand  # Car brand
        self.model = model  # Specific model of the car
        self.description = description  # Clearly and concisely describes the car
        self.unit_price = unit_price  # Price in quetzales for each car
        self.quantity = quantity  # Integer that describes how many units are available at the dealership
        self.image = image  # URL of the car's image
