class Restaurant:
    def __init__(self, restaurant_name, cuisine_type ):
        self.restaurant_name = restaurant_name
        self.cuisine_type= cuisine_type

    def describe_restaurant(self):
        print(f"Nama restoran: {self.restaurant_name}")
        print(f"Jenis makanan: {self.cuisine_type}")

    def ope_restaurant(self):
        print(f"{self.restaurant_name} sedang buka!")

#membuat instans
restaurant = Restaurant("Warung padang", "masakan padang")

#mencetak atribut secara terpisah
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

#memanggil metode
restaurant.describe_restaurant()
restaurant.ope_restaurant()