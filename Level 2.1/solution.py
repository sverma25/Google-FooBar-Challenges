def answer(h, q):
    # your code here
    def calculate_parent_node(q, tree_root = 2**h - 1, depth = h):
        right_node = tree_root - 1
        left_node = tree_root - (2**(depth-1))
        #print(q, depth, tree_root, left_node, right_node)

        # Node does not exist, or is the root node
        if (q == tree_root):
            #print("Root Node\n")
            return -1
        # Node is the left or right child node of the root
        elif (q == right_node or q == left_node):
            #print("Child Node\n")
            return tree_root
        # Node value > left node, => left subtree
        # Otherwise, => right tree
        elif (q < left_node):
            #print("Left subtree")
            return calculate_parent_node(q, left_node, depth-1)
        else:
            #print("Right subtree")
            return calculate_parent_node(q, right_node, depth-1)

    return list(map(calculate_parent_node, q))

#print(answer(3, [1, 4, 7])) #[3, 6, -1].
#print(answer(3, [7, 3, 5, 1])) #[-1, 7, 6, 3]
#print(answer(5, [19, 14, 28])) #[21, 15, 29]
