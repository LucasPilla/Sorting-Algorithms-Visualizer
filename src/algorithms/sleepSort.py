def sleepSort(array, left, right):
   
    place = [0]
    maxNum = max(array)
    
    copyArray = array.copy()
    # Sort the events based on sleep_time

    #time passing
    for i in range(maxNum + 1):
        for j in range(len(copyArray)):
            if copyArray[j] == i:
                array[place[0]] = copyArray[j]
                yield array, place[0], j, -1, -1
                print(f"{array}: {place[0]}")
                place[0] += 1


    # Yield the final sorted array
    yield array, -1, -1, -1, -1
    