'''
with open ("example.txt","r") as f:
    data = f.read()
    print(data)


file = open("example.txt", "a")
data = file.write("File handling \n")
file.close()
'''
with open("example.txt", "a+") as f:
    data = f.write("Indore")
    f.seek(0)
    data = f.readlines()
    print(data)