def bucketSort(array, *args):
    """
    Bucket sort.

    Distributes values into buckets, sorts each bucket (here with Python's ``sorted``),
    then concatenates. Performance depends on how evenly keys spread across buckets.

    Time complexity: O(n + k) average when keys are uniformly spread across k buckets; can degrade to O(n²) with bad distributions (n is the number of elements).
    """
    # Create buckets
    bucket = []
    for i in range(len(array)):
        bucket.append([])
    n = len(bucket)

    # Assign values to buckets
    for j in array:
        index_b = int(j/n)
        bucket[index_b].append(j)
        yield array, (j,), (index_b,)

    # Sort each bucket
    for i in range(len(array)):
        bucket[i] = sorted(bucket[i])

    # Merge the buckets to create the sorted array
    k = 0
    for i in range(len(array)):
        for j in range(len(bucket[i])):
            yield array, (k,), (i,)
            array[k] = bucket[i][j]
            k += 1
