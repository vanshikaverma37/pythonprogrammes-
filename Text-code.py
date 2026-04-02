'''
with open("Butterflyy.txt","r") as file:
    data = file.read()
    print(data)

with open("Butterflyy.txt", "a+") as file:
    data = file.write("print(\"The Butterfly\")")
    file.seek(0)
    print(file.read())

'''
with open("Butterflyy.txt","r")as file:
    exec(file.read())