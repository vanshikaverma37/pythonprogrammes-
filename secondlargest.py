a = [4,5,6,2,9,3]
first, sec= a[0], a[0]
for i in range(len(a)):
    if a[i] >= first:
        sec = first
        first = a[i]
        

    if a[i]>= sec and first != a[i]:
        sec = a[i]
print(sec)