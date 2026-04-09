def anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    
    freq_counter1 = {}
    freq_counter2 = {}
     
    for char in str1:
        if char in freq_counter1:
            freq_counter1[char] += 1
        else:
            freq_counter1[char] = 1

    for char in str2:
        if char in freq_counter2:
            freq_counter2[char] += 1
        else:
            freq_counter2[char] = 1

    for key in freq_counter1:
        if key not in freq_counter2:
            return False
        if freq_counter2[key] != freq_counter1[key]:
            return false
    return True
print(anagram('anagram', 'nagaram'))