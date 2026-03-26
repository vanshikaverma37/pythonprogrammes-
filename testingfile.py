a = 121
aa =str(a)
c = 0
for i in range(len(str(a))):
    b = a%10
    a = a//10
    c = c * 10 + b
print(aa[::-1])
if aa[::-1]==str(c):
    print("palindrome done")
else:       
    print(" not palindrome")