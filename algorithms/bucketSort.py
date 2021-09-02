def bucketSort(array, *args):
    bucket = []
    for i in range(len(array)):
        bucket.append([])
    n = len(bucket)
    
    for j in array:
        index_b = int(j/n)
        bucket[index_b].append(j)
        yield array, j, -1, index_b, -1

    for i in range(len(array)):
        bucket[i] = sorted(bucket[i])
    
    k = 0
    for i in range(len(array)):
        for j in range(len(bucket[i])):
            yield array, k, -1, i, -1
            array[k] = bucket[i][j]
            k += 1
