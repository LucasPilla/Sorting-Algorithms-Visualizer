def bucketSort(array):
    """
    Bucket Sort is a sorting algorithm that works by partitioning 
    an array into smaller buckets, sorting each bucket either by 
    recursively applying the Bucket Sort algorithm or using another 
    sorting algorithm, and then concatenating the sorted buckets 
    to form the final sorted array. 
    
    Time complexity: O(n+k), where n is the number of elements to be sorted 
    and k is the number of buckets used, but can be as bad as O(n^2) if the elements 
    are not uniformly distributed among the buckets.
    
    :param array: The list to be sorted.
    :return: The sorted list.
    """
    # Find the minimum and maximum values in the array
    min_val, max_val = min(array), max(array)
    
    # Create buckets
    num_buckets = len(array)
    bucket = [[] for _ in range(num_buckets)]
    
    # Assign values to buckets
    for value in array:
        # Determine which bucket to place the value in
        index_b = int((value - min_val) / (max_val - min_val + 1) * num_buckets)
        bucket[index_b].append(value)
        yield array, value, -1, index_b, -1

    # Sort each bucket (we'll use a different sorting algorithm, e.g., insertion sort)
    for i in range(num_buckets):
        bucket[i] = sorted(bucket[i])

    # Merge the buckets to create the sorted array
    k = 0
    for i in range(num_buckets):
        for value in bucket[i]:
            yield array, k, -1, i, -1
            array[k] = value
            k += 1

