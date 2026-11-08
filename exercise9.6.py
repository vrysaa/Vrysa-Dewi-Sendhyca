class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Nama restoran: {self.restaurant_name}")
        print(f"Jenis masakan: {self.cuisine_type}")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["Vanilla", "Cokelat", "Stroberi", "Matcha"]

    def display_flavors(self):
        print("Daftar rasa es krim:")
        for flavor in self.flavors:
            print(f"- {flavor}")

#membuat instans IceCreamStand
ice_cream = IceCreamStand("Sweet Ice Cream", "es krim")

#memanggil metode
ice_cream.describe_restaurant()
ice_cream.display_flavors()