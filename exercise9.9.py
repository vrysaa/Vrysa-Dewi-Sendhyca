
class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"Mobil ini memiliki baterai {self.battery_size}-kWh.")

    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        else:
            range = 0

        print(f"Mobil dapat menempuh jarak sekitar {range} mil.")

    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65


class ElectricCar:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.battery = Battery()

    def describe_car(self):
        print(f"Mobil: {self.make} {self.model}")
        print(f"Tahun: {self.year}")

    def get_range(self):
        self.battery.get_range()


# Membuat mobil listrik dengan baterai default
my_car = ElectricCar("Tesla", "Model S", 2024)

# Menampilkan informasi mobil
my_car.describe_car()

# Menampilkan jarak tempuh sebelum upgrade
print("\nSebelum upgrade:")
my_car.get_range()

# Melakukan upgrade baterai
my_car.battery.upgrade_battery()

# Menampilkan jarak tempuh setelah upgrade
print("\nSetelah upgrade:")
my_car.get_range()