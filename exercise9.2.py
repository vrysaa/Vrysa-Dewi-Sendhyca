class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Nama restora: {self.restaurant_name}")
        print(f"jenis makanan: {self.cuisine_type}")

#membuat 3 instant restoran
restaurant1 = Restaurant("warung padang", "masakan padang")
restaurant2 = Restaurant("sushi hiro", "masakan jepang")
restaurant3 = Restaurant("pizza hut", "masakan italia")

#memanggil metode untuk tiap instans
restaurant1.describe_restaurant()
print()

restaurant2.describe_restaurant()
print()

restaurant3.describe_restaurant()
print()