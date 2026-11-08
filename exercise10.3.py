#kode sebelum disederhanakan
filename = 'learning_python.txt'

with open(filename) as file_object:
    contents = file_object.read()

lines = contents.splitlines()

for line in lines:
    print(line)

#kode setelah disederhanakan
filename = 'learning_python.txt'

with open(filename) as file_object:
    contents = file_object.read()

for line in contents.splitlines():
    print(line)