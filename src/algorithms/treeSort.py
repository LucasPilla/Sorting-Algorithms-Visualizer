class Node:
    def __init__(self, val, pos):
        """
        Initialize a new instance of the Node class.
        """
        self.l, self.r = None, None
        self.pos = pos
        self.val = val

    def display(self, res):
        """
        Traverse the binary search tree in-order and append the values to the given list.
        """
        if self.l:
            self.l.display(res)
            self.l = None
        res.append(self.val)
        if self.r:
            self.r.display(res)


def treeSort(array, *args):
    """
    Tree Sort is a sorting algorithm that builds a binary search tree from 
    the elements of the array to be sorted. For each element in the input array, 
    the algorithm inserts the element into the tree. Once all the elements are 
    inserted, the algorithm performs an in-order traversal of the tree, 
    which yields the sorted array.
    
    Time complexity: ranges from O(n) to O(n^2) depeding on the shape of
    the binary tree 
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
