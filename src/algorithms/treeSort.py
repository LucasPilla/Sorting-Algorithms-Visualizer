class Node:
    def __init__(self, val, pos):
        self.l, self.r = None, None
        self.pos = pos
        self.val = val

    def display(self, res):
        if self.l:
            self.l.display(res)
            self.l = None
        res.append(self.val)
        if self.r:
            self.r.display(res)


def treeSort(array, *args):
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
