class Node:
    def __init__(self, val, pos):
        """BST node storing *val* and *pos*."""
        self.l, self.r = None, None
        self.pos = pos
        self.val = val

    def display(self, res):
        """In-order traversal; append values to *res* (destructively clears left links)."""
        if self.l:
            self.l.display(res)
            self.l = None
        res.append(self.val)
        if self.r:
            self.r.display(res)


def treeSort(array, *args):
    """
    Tree sort (BST sort).

    Inserts each element into a binary search tree, then reads values with an in-order walk.

    Time complexity: O(n log n) when the tree stays balanced; O(n²) if insertions skew the tree (e.g. sorted input).
    """
    root = None
    for i in range(len(array)):
        if root is None:
            root = Node(array[i], i)
            yield array, (i,), ()
            continue
        current = root
        while True:
            if current.val > array[i]:
                if current.l:
                    current = current.l
                    continue
                current.l = Node(array[i], i)
                yield array, (i, current.pos), ()
                break
            if current.r:
                current = current.r
                continue
            current.r = Node(array[i], i)
            yield array, (i, current.pos), ()
            break
    res = []
    root.display(res)
    yield res, (), ()
