# Given a list of integers, find the highest product you can 
# get from three of the integers.

# The input list_of_ints will always have at least three 
# integers.

def find_highest_product(list_of_ints):
    max_product = 0
    for i in range(0, len(list_of_ints)-2):
        for j in range(i+1, len(list_of_ints)-1):
            for k in range(i+2, len(list_of_ints)):
                current_product = list_of_ints[i]*list_of_ints[j]*list_of_ints[k]
                if current_product > max_product:
                    current_product = max_product
    return max_product

print(find_highest_product([1, 1, 1, 2]))
