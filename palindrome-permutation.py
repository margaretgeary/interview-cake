def find_permutation_palindrome(word):

    unpaired_char = set() 

    # Track characters we've seen an odd number of times
    
    for letter in word:
        if letter in unpaired_char:
            unpaired_char.remove(letter)
        else:
            seen_letters.add(letter)

    # The string has a palindrome permutation if it
    # has one or zero characters without a pair
    return len(unpaired_characters) <= 1



print(find_permutation_palindrome("civic"))
print(find_permutation_palindrome("ivicc"))
print(find_permutation_palindrome("civil"))
print(find_permutation_palindrome("livci"))
