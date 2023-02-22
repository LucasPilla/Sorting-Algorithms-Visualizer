def bucketSort(array, *args):
    """
    Sorts an array of integers using Bucket Sort Algorithm.

    Bucket Sort works by partitioning an array into a number of smaller 
    "buckets". Each bucket is then sorted individually, either using 
    another sorting algorithm or by recursively applying the bucket sort algorithm. 
    Once all the buckets are sorted, the contents of the buckets are concatenated 
    to form the final sorted array.

    Bucket Sort is typically used when the input is uniformly distributed 
    over a range, allowing for efficient partitioning into buckets. It has an 
    average case time complexity of O(n+k), where n is the number of elements 
    in the input array and k is the number of buckets used. However, 
    its worst-case time complexity is O(n^2), which occurs when all 
    the elements are in the same bucket.

    Args:
        array (list): The array of integers to be sorted.

    Yields:
        tuple: A tuple containing the updated array, and information on the two elements being compared in each iteration of the algorithm.
            The tuple is of the format (array, index1, index2, bucketIndex, -1).
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
