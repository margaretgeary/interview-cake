#---------------------O(n^2)-----------------------

def merge_orders(takeout_orders, dinein_orders, served_orders):

    if len(served_orders) == 0:
        return True
    if len(takeout_orders) and takeout_orders[0] == served_orders[0]:
        return merge_orders(takeout_orders[1:], dinein_orders, served_orders[1:])
    elif len(dinein_orders) and dinein_orders[0] == served_orders[0]:
        return merge_orders(takeout_orders, dinein_orders[1:], served_orders[1:])
    else:
        return False


print(merge_orders([17, 18, 24], [12, 19, 20], [17, 8, 12, 19, 24, 2]))

#----------------O(1)----------------------------

def merge_orders(takeout_orders, dinein_orders, served_orders):
    i=0
    j=0
    takeout_orders_max_i = len(takeout_orders) - 1
    dinein_orders_max_j = len(dinein_orders) - 1
    
    for order in served_orders:
        if i <= takeout_orders_max_i and order == takeout_orders[i]:
            i += 1
        if j <= dinein_orders_max_j and order == dinein_orders[j]:
            j += 1
        else:
            return False
    if j != len(dinein_orders) or i != len(takeout_orders):
        return False
    return True