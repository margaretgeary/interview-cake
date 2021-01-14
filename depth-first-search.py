# Write a function to see if a binary tree ↴ is "superbalanced" 
# (a new tree property we just made up).

# A tree is "superbalanced" if the difference between the depths 
# of any two leaf nodes ↴ is no greater than one.

def is_balanced(tree_root):
    
    if tree_root is None:
        return True
    #A tree with no nodes is superbalanced, since there are no leaves

    depths = []
    #short-circuit as soon as we find more than 2

    nodes = []
    nodes.append((tree_root, 0))
    #we'll treat this list as a stack that will store tuples of (node, depth)

    while len(nodes):
        node, depth = nodes.pop()
        # pop a node and its depth from the top of our stack

        if (not node.left) and (not node.right):
            #case: we found a leaf
            if depth not in depths:
                depths.append(depth)
                #we only care if it's a new depth

                if ((len(depths) > 2) or (len(depths == 2 and abs(depths[0] - depths[1]) > 1)):
                    return False
                # tree is unbalanced if we have more than two depths, or if the difference between depths
                # is more than one

        else:
            if node.left:
                nodes.append(node.left, depth + 1)
            if node.right
                nodes.append(node.right, depth + 1)

    return True


        