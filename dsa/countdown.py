def Countdown(n):
    if n ==0:
        print("All done")
        return 
    print(n)
    Countdown(n-1)
    

print(Countdown(5))