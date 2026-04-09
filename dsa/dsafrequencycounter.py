def same(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    
    freq_counter1 = {}
    freq_counter2 = {}
     
    for val in arr1:
        if val in freq_counter1:
            freq_counter1[val] += 1
        else:
            freq_counter1[val] = 1

    for val in arr2:
        if val in freq_counter2:
            freq_counter2[val] += 1
        else:
            freq_counter2[val] = 1

    for key in freq_counter1:
        if key**2  not in freq_counter2 :
            return False
        if freq_counter2[key ** 2] != freq_counter1[key]:
            return False
    
    return True
        
print(same([1,2,3],[1,4,8]))