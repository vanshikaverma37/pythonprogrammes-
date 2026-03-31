a = [4,5,6,2,9,3,2,5,6,4]

for i in range(len(a)):
    countt = 0
    for j in range(len(a)):

        if a[j] == a[i]:
            countt+=1
    print("count of ", a[i]," is :", countt)
            
     
            


        
