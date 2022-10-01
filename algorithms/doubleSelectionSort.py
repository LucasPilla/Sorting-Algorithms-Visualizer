def doubleSelectionSort(array, *args):
    size = len(array)
    minIndex = 0
    maxIndex = size-1
    min = array[minIndex]
    max = array[maxIndex]
    newMinIndex = minIndex + 1 
    newMaxIndex = maxIndex 
    for i in range (size-1): 
        minIndex = i 
        maxIndex = size-1 
        min = array[minIndex] 
        max = array[maxIndex] 
        while( minIndex < maxIndex): 
            min = array[minIndex]
            max = array[maxIndex]
            newMinIndex = minIndex+1
            newMaxIndex = maxIndex

            for index in range(newMinIndex, newMaxIndex): 
                yield array, index, newMinIndex, newMaxIndex, -1; 
                value = array[index]
                if(value <= min): 
                    if(value < min):
                        min = value
                        newMinIndex = minIndex
                        array[index] = array[newMinIndex]
                    else: 
                        array[index] = array[newMinIndex]
                        ++index
                    array[newMinIndex] = value
                    ++newMinIndex
                elif(value >= max):
                    if(value > max): 
                        max = value
                        newMaxIndex = maxIndex
                    array[index] = array[newMaxIndex]
                    array[newMaxIndex] = value
                    --newMaxIndex
                else: 
                    ++index
            minIndex = newMinIndex
            maxIndex = newMaxIndex
        