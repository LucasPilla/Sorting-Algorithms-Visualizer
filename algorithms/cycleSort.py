from display import handleDrawing


def cycleSort(array, *args):
    #swaps = 0

    for cycle_start in range(0, len(array) - 1):
        item = array[cycle_start]

        pos = cycle_start
        item = array[pos]
        for i in range(pos + 1, len(array)):
            if array[i] < item:
                pos += 1

        if pos == cycle_start:
            continue

        while array[pos] == item:
            pos += 1

        array[pos], array[cycle_start] = array[cycle_start], array[pos]
        handleDrawing(array, cycle_start, pos, -1, -1)
        #swaps = swaps+1

        while pos != cycle_start:
            pos = cycle_start
            item = array[pos]
            for i in range(pos + 1, len(array)):
                if array[i] < item:
                    pos += 1

            if pos == cycle_start:
                continue

            while array[pos] == item:
                pos += 1

            array[pos], array[cycle_start] = array[cycle_start], array[pos]
            handleDrawing(array, cycle_start, pos, -1, -1)
            #swaps = swaps + 1
