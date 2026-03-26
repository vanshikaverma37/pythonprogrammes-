'''
n= 100
if n>0:
    for i in range(len(str(n))):
        i +=1
    print(i)
elif n==0:
    print(1)
else:
    for i in range(len(str(n))):
        i +=1
    print(i-1)
  
    

n = -1000000
if n>0:
    count = 0
    for i in str(n):
        n= n//10
        count+=1
    print(count)
elif n==0:
    print(1)
else:
    count = -1
    for i in str(n):
        n= n//10
        count+=1
    print(count)
'''
n= 1999;
count = 0
while n>0:
    n = n//10
    count+=1
print(count)

