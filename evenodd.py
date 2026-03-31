a = [4,5,6,2,9,3]
count_even, count_odd = 0, 0
for i in range(len(a)):
    if a[i] %2 ==0:
        count_even +=1
    else:
        count_odd += 1

    
print("even = ", count_even, "odd = ", count_odd)