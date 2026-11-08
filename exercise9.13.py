
from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))


# Membuat dadu bersisi 6
print("Dadu 6 sisi:")
die1 = Die()

for i in range(10):
    die1.roll_die()


# Membuat dadu bersisi 10
print("\nDadu 10 sisi:")
die2 = Die(10)

for i in range(10):
    die2.roll_die()


# Membuat dadu bersisi 20
print("\nDadu 20 sisi:")
die3 = Die(20)

for i in range(10):
    die3.roll_die()