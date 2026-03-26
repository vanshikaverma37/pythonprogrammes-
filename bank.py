x = 2550;
balance = 600;
if x%5==0 :
    if balance>= x+0.50:
        balance = balance - x - 0.50;
        print(balance)
        print('Transaction successful');
    else:   print('you do not have suffiecient balance');
else: print("This is not a multiple of 5")




