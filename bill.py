x = 250;
if x >50 :
    charge = 0.50*50
    x = x-50
    if x>100:
        charge = charge + 0.75*100
        x = x-100
        if x>100:
            charge = charge + 1.20*100
            x = x-100
        elif x<=100:
            charge = charge+1.20*x
    elif x<=100:
        charge = charge+0.750*x
elif x<=50:
    charge = 0.50*x




charge = charge  + 0.20*charge

print(charge)