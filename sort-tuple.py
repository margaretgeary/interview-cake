## to merge two tuples, add them together

# a[start:stop]  # items start through stop-1
# a[start:]      # items start through the rest of the array
# a[:stop]       # items from the beginning through stop-1
# a[:]           # a copy of the whole array

#-------------------------MY ATTEMPT-----------------------------

# def merge_ranges(unsorted_tuples):
#     # new_tuples = []
#     # list_of_tuples = sorted(unsorted_tuples)
#     # for i in range(0, len(list_of_tuples)-1):
#     #     for j in range(i+1, len(list_of_tuples)):
#     #         if list_of_tuples[i][1] >= list_of_tuples[j][0]:
#     #             print(new_tuples)
#     #             consolidated_tuples = list_of_tuples[i] + list_of_tuples[j]
#     #             result_tuple = consolidated_tuples[0], consolidated_tuples[-1]
#     #         else:
#     #             new_tuples.append(list_of_tuples[i])
#     # print(new_tuples)


# print(merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]))

#----------------------------SOLUTION------------------------------


def merge_ranges(unsorted_tuples):
    
    list_of_tuples = sorted(unsorted_tuples)  # [(0, 1), (3, 5), (4, 8), (9, 10), (10, 12)]

    merged_tuples = [list_of_tuples[0]]  # [(0, 1)], initializing list that contains starting tuple
    # print(merged_tuples)

    for current_tuple_start, current_tuple_end in list_of_tuples[1:]: # iterate two by two
        last_merged_tuple_start, last_merged_tuple_end = merged_tuples[-1] #*********
        print(merged_tuples[-1])
        
        if current_tuple_start <= last_merged_tuple_end:
            merged_tuples[-1] = (last_merged_tuple_start, max(last_merged_tuple_end, current_tuple_end))
        else:
            merged_tuples.append((current_tuple_start, current_tuple_end))
        
    # return merged_tuples


print(merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]))
