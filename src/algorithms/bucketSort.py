def bucketSort(array, *args):
    """
    Bucket Sort is a sorting algorithm that works by partitioning 
    an array into smaller buckets, sorting each bucket either by 
    recursively applying the Bucket Sort algorithm or using another 
    sorting algorithm, and then concatenating the sorted buckets 
    to form the final sorted array. 
    
    Time complexity: O(n+k), where n is the number of elements to be sorted 
    and k is the number of buckets used, but can be as bad as O(n^2) if the elements 
    are not uniformly distributed among the buckets.
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
        yield array, j, -1, index_b, -1

    # Sort each bucket
    for i in range(len(array)):
        bucket[i] = sorted(bucket[i])

    # Merge the buckets to create the sorted array
    k = 0
    for i in range(len(array)):
        for j in range(len(bucket[i])):
            yield array, k, -1, i, -1
            array[k] = bucket[i][j]
            k += 1
