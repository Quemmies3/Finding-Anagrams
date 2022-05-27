# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
   # Convert string into lists  
    list1 = list(word)  
    list2 = list(anagram)  
    # Sort the list value  
    list1.sort()  
    list2.sort()  

    position = 0  
    matches = True 

    while position < len(word) and matches:  
        if list1[position]==list2[position]:  
            position = position + 1  
        else:  
            matches = False  

    return matches

print(find_anagram('listen','silent'))

