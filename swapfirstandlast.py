n = 487845;
num = 0
for i in range(len(str(n))):
    a= n%10
    
    num = num +a
    n= n//10
print(num)