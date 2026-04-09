def same(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    for i in range(len(arr1)):
        value = arr1[i] ** 2
        
        if value in arr2:
            arr2.remove(value) 
        else:
            return False
    
    return True
ar1 = [1, 2, 3]
ar2 = [1, 4, 9]

print(same(ar1, ar2))