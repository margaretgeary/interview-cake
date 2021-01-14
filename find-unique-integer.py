def find_unique_integer(list):

    numbers_dictionary = {}

    for num in list:
        numbers_dictionary[num] = numbers_dictionary.get(num, 0) + 1

    for num, count in numbers_dictionary.items():
        if count == 1:
            return num

    return False
    
print(find_unique_integer([1,1,1,1,1]))


# def make_letter_counts_dict(phrase):
#     """Return dict of letters and # of occurrences in phrase."""

#     letter_counts = {}

#     for letter in phrase:
#         letter_counts[letter] = letter_counts.get(letter, 0) + 1

#     return letter_counts
