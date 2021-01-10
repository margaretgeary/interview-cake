# Write a function that takes a list of characters and 
# reverses the letters in place. 

#reversed(list) will reverse letters

def reverse_list(list):
    reversed_list = []
    for letter in reversed(list):
        reversed_list.append(letter)
    return reversed_list

print(reverse_list(["d", "o", "g"]))


#---------------SOLUTION-------------------------

def swap_list(list):

    left_index = 0
    right_index = len(list)-1

    while left_index < right_index:

        #swap chars
        list[left_index], list[right_index] = \
            list[right_index], list[left_index]

        #move toward middle
        left_index += 1
        right_index -= 1

print(swap_list("d", "o", "g"))