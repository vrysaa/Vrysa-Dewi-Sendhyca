current_users = ['vrysa', 'lana', 'kala', 'djilva', 'ren']
new_users = ['VRYSA', 'hanin', 'mareta', 'REN', 'najmah']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry, {new_user} is already taken. Please enter a new username.")
    else:
        print(f"Great, {new_user} is available!")