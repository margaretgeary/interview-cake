def find_inflection_point(words):
    floor_index = -1
    ceiling_index = len(words)

    while floor_index + 1 < ceiling_index:
        distance = ceiling_index - floor_index
        half_distance = distance // 2
        guess_index = floor_index + half_distance
        guess_value = words[guess_index]

        if guess_value >= words[0]:
            floor_index = guess_index

        if guess_value <= words[0]:
            ceiling_index = guess_index

        if floor_index + 1 == ceiling_index:
            return ceiling_index


print(find_inflection_point([
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'asymptote',
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
]))

# Binary search teaches us that when a list is sorted or mostly sorted:

# The value at a given index tells us a lot about what's to the left and what's to the right.
# We don't have to look at every item in the list. By inspecting the middle item, we can "rule out" half of the list.
# We can use this approach over and over, cutting the problem in half until we have the answer. This is sometimes called "divide and conquer."
# So whenever you know a list is sorted or almost sorted, think about these lessons from binary search and see if they apply.
