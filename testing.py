def sleepSort(array, left, right):
   
    place = [0]
    maxNum = max(array)
    
    if not array:
        return    
    # Sort the events based on sleep_time
    
    #time passing
    for i in range(maxNum):
        for j in range(array):
            if array[j] == i:
                array[place[0]] = array[j]
                #yield array, place[0], j, -1, -1
                place[0] += 1
                
            
            
        # Simulate the processing of the element at the appropriate time
        # print(f"The index: {index} and the Value: {sleepTime}")
        # array[place[0]] = sleepTime
        # yield array, place[0], index, -1, -1
        # place[0] += 1

    # Yield the final sorted array
    yield array, -1, -1, -1, -1
    print(array)
    

array = [1, 4, 5, 2, 8, 0, 1]

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
print("Final array")
print(array)

