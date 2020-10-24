from display import handleDrawing


def countingSort(array, *args):
    size = len(array)
    A = array.copy()
    C = [0]*(max(A)+1)
    for i in range(size):
        C[A[i]] += 1
    for i in range(1, len(C)):
        C[i] += C[i-1]
    for i in range(0, size):
        handleDrawing(array, C[A[size-i-1]]-1, -1, size-i-1, -1)
        array[C[A[size-i-1]]-1] = A[size-i-1]
        C[A[size-i-1]] -= 1
