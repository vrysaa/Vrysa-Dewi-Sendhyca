
def make_car(manufacturer, model, **car_info):
    car = {
        "manufacturer": manufacturer,
        "model": model
    }

    for key, value in car_info.items():
        car[key] = value

    return car


# Membuat informasi mobil
car = make_car(
    "subaru",
    "outback",
    color="blue",
    tow_package=True
)

# Mencetak dictionary mobil
print(car)