
def patienceSort(array, *args):
    def getLowestElement(arrStacks: list):
        lowest = float('inf')
        index = -1

        for i in range(len(arrStacks)):
            elemen = arrStacks[i][len(arrStacks[i]) - 1]
            if (elemen < lowest):
                index = i
                lowest = elemen

        arrStacks[index].pop()

        if len(arrStacks[index]) == 0:
            del arrStacks[index]

        return lowest
        
    i = 0
    arrStacks = list()
    inserted: bool
    size: int = len(array)
    yield array, 0,0,-1,-1
    for num in (array):
        inserted = False
        for stack in (arrStacks):
            if not inserted and stack[len(stack) - 1] >= num:
                stack.append(num)
                inserted = True
        if not inserted:
            arrStacks.append([num])

    array=[0 for i in range(size)]

    for i in range(size):
        array[i]=getLowestElement(arrStacks)
        yield array, i, i+1, -1, -1
    del i
