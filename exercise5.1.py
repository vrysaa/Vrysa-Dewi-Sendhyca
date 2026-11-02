
car = 'subaru'

# 5 pengujian True
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car != 'toyota'? I predict True.")
print(car != 'toyota')

print("\nIs car.lower() == 'subaru'? I predict True.")
print(car.lower() == 'subaru')

print("\nIs len(car) == 6? I predict True.")
print(len(car) == 6)

print("\nIs car.startswith('sub')? I predict True.")
print(car.startswith('sub'))

# 5 pengujian False
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

print("\nIs car != 'subaru'? I predict False.")
print(car != 'subaru')

print("\nIs car == 'SUBARU'? I predict False.")
print(car == 'SUBARU')

print("\nIs len(car) == 5? I predict False.")
print(len(car) == 5)

print("\nIs car.endswith('toyota')? I predict False.")
print(car.endswith('toyota'))