
n = 5
for i in range(0, n+1):
    for j in range(0,i):
        print("*", end="")
    print(" ")
print()
n = 5
for i in range(n,0,-1):
    for j in range(0,i):
        print("*", end="")
    print(" ")

print()
n = 5
for i in range(0, n+1):
    for j in range(n,i,-1):
        print(" ", end="")
    for j in range(0,i):
        print("*", end="")
    print(" ")
print()

n = 5
for i in range(0, n):
    for j in range(0,i):
        print(" ", end="")
    for j in range(n,i,-1):
        print("*", end="")
    print(" ")



