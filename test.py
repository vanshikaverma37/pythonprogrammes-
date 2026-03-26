n = 56457;
for i in range(len(str(n))):
    a = n%10
    n = n//10
    print(a,end="")