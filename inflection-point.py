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
