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
       
  def appendStacksToList(arr, arrStacks):
    for stack in (arrStacks):
      for element in (stack):
        arr.append(element)
    
  
   
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
          
  array.clear()
  
  for i in range(size):
    lowest=getLowestElement(arrStacks)
    array.append(lowest)
    appendStacksToList(array, arrStacks)
    yield array, i, i+1, -1, -1
    del array[i+1:]
