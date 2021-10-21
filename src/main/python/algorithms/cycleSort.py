def cycleSort(array, *args):
    for cycle_start in range(0, len(array) - 1):
        item = array[cycle_start]
        pos = cycle_start
        
        for i in range(cycle_start + 1, len(array)):
            if array[i] < item:
                pos += 1

        if pos == cycle_start:
            continue

        while array[pos] == item:
            pos += 1
        yield array, cycle_start, pos, -1, -1
        array[pos], item = item, array[pos]

        while pos != cycle_start:
            pos = cycle_start
            for i in range(cycle_start + 1, len(array)):
                if array[i] < item:
                    pos += 1

            while array[pos] == item:
                pos += 1
            yield array, cycle_start, pos, -1, -1
            array[pos], item = item, array[pos]
