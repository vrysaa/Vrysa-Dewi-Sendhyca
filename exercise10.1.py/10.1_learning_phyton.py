filename = 'learning_python.txt'

#membaca seluruh isi file
with open(filename) as file_object:
    contents = file_object.read()
print(contents)

#membaca file dan menyimpan setiap baris ke dalam list
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())