a = [4,5,2,9,3]
max, min = a[0], a[0]
for i in range(len(a)):
    if a[i] > max:
        max = a[i]
    elif a[i] < min:
        min = a[i]
print(max, min)