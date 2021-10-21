def pigeonholeSort(array, *args):
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
