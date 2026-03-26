import math
a = 145
aa=a
factt = 0
for i in range(len(str(a))):
    b = a%10
    a = a//10
    factt = factt+ math.factorial(b)
print(factt)
if aa == factt:
    print(factt,"strong")
else:
    print(factt,"not strong")