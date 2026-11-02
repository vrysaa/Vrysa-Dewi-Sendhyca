#pengujian kesetaraan dan ketidaksetaraan string
car = 'subaru'

print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car != 'subaru'? I predict False.")
print(car != 'subaru')

#pengujian menggunakan metode lower()
name = 'VRYSA'

print("Is name.lower() == 'vrysa'? I predict True")
print(name.lower() == 'vrysa')

print("Is name.lower() == 'VRYSA'? I predict False")
print(name.lower() == 'VRYSA')

#pengujiannumerik
umur = 18

print("\nIs umur == 18? I predict True")
print(umur == 18)

print("\nIs umur != 18? I predict False")
print(umur != 18)

print("\nIs umur > 15? I predict True")
print(umur > 15)

print("\nIs umur < 15? I predict False")
print(umur < 15)

print("\nIs umur >= 18? I predict True")
print(umur >= 18)

print("\nIs umur <= 15? I predict False")
print(umur <= 15)

#pengujian menggunakan and dan or
umur = 20
print("\nIs umur > 18 and umur < 25? I predict True.")
print(umur > 18 and umur < 25)

print("\nIs umur > 25 and umur < 30? I predict False.")
print(umur > 25 and umur < 30)

print("\nIs umur < 18 or umur == 20? I predict True.")
print(umur < 18 or umur == 20)

print("\nIs umur < 18 or umur > 25? I predict False.")
print(umur < 18 or umur > 25)

#pengujian apakah item ada di dalam list
buah = ['melon', 'stroberi', 'mangga']

print("\nIs 'melon' in buah? I predict True")
print('melon' in buah)

print("\nIS 'mangga' in buah? I predict True")
print('apel' in buah)

#pengujian apakah item tidak ada di dalam list
buah = ['melon', 'stroberi', 'mangga']

print("\nIs 'apel' in buah? I predict False")
print('apel' in buah)

print("\nIs 'pisang' in buah? I predict False")
print('pisang' in buah)