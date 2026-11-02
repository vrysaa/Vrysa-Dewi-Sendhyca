pizzas = ['pepperoni', 'cheese', 'beef']

friend_pizzas = pizzas.copy()

pizzas.append('mushroom')
friend_pizzas.append('chicken')

print("Pizza favorit saya adalah:")

for pizza in pizzas:
    print(pizza)

print("\nPizza favorit teman saya adalah:")

for pizza in friend_pizzas:
    print(pizza)