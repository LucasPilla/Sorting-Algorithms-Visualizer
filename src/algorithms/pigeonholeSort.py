def pigeonholeSort(array, *args):
  """
  Sorts an array in ascending order using Pigeonhole Sort Algorithm.

  Pigeonhole Sort is a sorting algorithm that is used to sort items 
  when they are limited to a range of values. The algorithm works by 
  placing each item in its corresponding pigeonhole. Then, the items 
  are sorted by finding the pigeonholes that contain items, in ascending 
  order. It is useful when the range of values in the array is small 
  compared to the size of the array, as it is a linear time sorting algorithm.

  Args:
    array: An array of integers to be sorted.
    *args: Optional arguments.

  Yields:
    Tuple containing the current state of the array, indices of the two elements being compared, and indices of the
    elements being modified.

  """

  minV = min(array)
  maxV = max(array)
  A = array.copy()
  size = maxV - minV + 1
  C = [0]*(size)
  i = 0
  for x in array:
    yield A, i, -1, -1, -1
    C[x - minV] += 1
    A[i] = A[i] / (C[x-minV] + 1)
    i += 1

  i = 0
  for count in range(size):
    while C[count] > 0:
        yield A, i-1, -1, C[count] * minV , -1
        C[count] -= 1
        array[i] = count + minV
        A[i] = array[i]
        i += 1
