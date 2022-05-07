# for pigeonholes, the indexes represent:
# the value from the array - the minimum value,
# and the item is the number of times that value is in the array
# we initialize the counts to 0
def pigeonholes(size):
  return [0]*size

def addTo(array, value):
  array[value] += 1

def subtractFrom(array, value):
  array[value] -= 1

def pigeonholeSort(array, *args):
  minValue = min(array)
  maxValue = max(array)
  rangeOfPossiblePigeonholes = maxValue - minValue + 1
  COUNTS = pigeonholes(rangeOfPossiblePigeonholes)

  # this yields array to be displayed and then
  # this counts each value in the "pigeonhole" array
  for step, value in enumerate(array):
    yield array, step, -1, -1, -1
    addTo(COUNTS, value - minValue)

  # this yields array to be displayed and then
  # this copies each value from the "pigeonhole" array
  step = -1
  for value in range(rangeOfPossiblePigeonholes):
    while COUNTS[value] > 0:
      yield array, step, -1, -1, -1
      subtractFrom(COUNTS, value)
      array[step] = value + minValue
      step += 1
