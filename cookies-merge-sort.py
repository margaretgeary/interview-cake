def merge_already_sorted_lists(my_list, alices_list):
    
    result_list = []

    while len(my_list) > 0 or len(alices_list) > 0:
        if my_list == []:
            result_list.append(alices_list.pop(0))
        elif alices_list == []:
            result_list.append(my_list.pop(0))
        elif my_list[0] < alices_list[0]:
            result_list.append(my_list.pop(0))
        else:
            result_list.append(alices_list.pop(0))
    
    return result_list


print(merge_already_sorted_lists([3, 4, 6, 10, 11, 15], [1, 5, 8, 12, 14, 19]))
