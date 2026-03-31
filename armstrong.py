

import math
a = 153
aa=a
num = 0
for i in range(len(str(a))):
    b = a%10
    a = a//10
    num = num+ math.pow(b,3)
print(num)
if aa == num:
    print(aa,"armstrong")
else:
    print(aa,"not armstrong")