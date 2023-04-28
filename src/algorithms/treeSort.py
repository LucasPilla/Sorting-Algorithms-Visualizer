class Node:
    def __init__(self, val, pos):
        """
        Initialize a new instance of the Node class.

        Args:
            val: The value of the node.
            pos: The position of the value in the original array.
        """
        self.l, self.r = None, None
        self.pos = pos
        self.val = val

    def display(self, res):
        """
        Traverse the binary search tree in-order and append the values to the given list.

        Args:
            res: The list to append the values to.
        """
        if self.l:
            self.l.display(res)
            self.l = None
        res.append(self.val)
        if self.r:
            self.r.display(res)


def treeSort(array, *args):
    """
    Sort the given array in ascending order using the Tree Sort algorithm.

    Tree Sort is a sorting algorithm that builds a binary search tree from 
    the elements of the array to be sorted, and then performs an in-order 
    traversal of the tree to obtain a sorted sequence.

    The algorithm starts by creating an empty binary search tree. 
    For each element in the input array, the algorithm inserts the element 
    into the tree. Once all the elements are inserted, the algorithm performs 
    an in-order traversal of the tree, which will visit the nodes in ascending 
    order, yielding the sorted array.

    The worst-case time complexity of Tree Sort is O(n^2) if the input array is 
    already sorted, and the best-case and average-case time complexity is O(n log n) 
    if the elements are inserted into the tree in a balanced manner. However, the space 
    complexity of Tree Sort is O(n), since it requires creating a binary search tree with n nodes.

    Args:
        array: The array to be sorted.

    Yields:
        A tuple with the current state of the array, the index of the current element being processed,
        and the positions of the left and right child nodes of the current node (or -1 if they don't exist).
        After the array is fully sorted, yields a tuple with the sorted array and -1 for the other values.
    """
    root = None
    for i in range(len(array)):
        if root is None:
            root = Node(array[i], i)
            yield array, i, -1, -1, -1
            continue
        current = root
        while True:
            if current.val > array[i]:
                if current.l:
                    current = current.l
                    continue
                current.l = Node(array[i], i)
                yield array, i, current.pos, -1, -1
                break
            if current.r:
                current = current.r
                continue
            current.r = Node(array[i], i)
            yield array, i, current.pos, -1, -1
            break
    res = []
    root.display(res)
    yield res, -1, -1, -1, -1
