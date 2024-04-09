import os

f = r"..\files"
list_f = list()

for root, dirs, files in os.walk(f):
    for file in files:
        if file not in list_f:
            list_f.append(os.path.join(root, file))
    for dir in dirs:
        if dir not in list_f:
            list_f.append(os.path.join(root, dir))
print(list_f)
