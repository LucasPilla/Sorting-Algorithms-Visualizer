from algorithms.binaryinsertionSort import binary_search

def calculate_min_run(n):
    """
	Calculate the minimum run length for TimSort algorithm.

    The minimum run length is calculated as follows:
		1. For any given n, a minimum run length is set to 32.
		2. A bitwise OR operation is performed on the last bit of the current n and last_bit.
		3. The current n is right-shifted by 1 bit to prepare for the next iteration.
		4. Steps 2 and 3 are repeated until n is less than the minimum run length.
		5. The last bit of the final n is added to the minimum run length to get the actual minimum run length.
    
    Args:
    	n (int): The length of the array to be sorted.

    Returns:
    	int: The minimum run length.
    """
    last_bit = 0
    RUN_LEN  = 32
    
    while n >= RUN_LEN:
        last_bit |= n & 1
        n >>= 1
        return n + last_bit

def binaryinsertionSort(array, start, end):
    """
	Perform binary insertion sort on a portion of the array.

    This function takes a slice of the array starting from index start and ending at index end, 
    and performs a binary insertion sort on that slice. It uses the binary_search function from the 
    binaryinsertionSort module to find the insertion point for each element in the slice.

    Args:
    	array (list): The array to be sorted.
    	start (int): The starting index of the slice to be sorted.
    	end (int): The ending index of the slice to be sorted.

    Yields:
    	tuple: A tuple containing the current state of the array, the start and end indices of the 
             slice being sorted, the index of the insertion point for the current element, and the 
             index of the current element.
    """
    for i in range(start, end + 1):
        val = array[i]
        j   = binary_search(array, val, start, i - 1, i)
        yield array, start, i-1, j, i
        array[0: len(array)] = array[: j] + [val] + array[j: i] + array[i + 1:]

def merge(arr, left, mid, right):
	"""
    This function merges two sorted portions of an array.

    Args:
		arr (list): The input array to be sorted.
		left (int): The starting index of the first sorted portion of the array.
		mid (int): The ending index of the first sorted portion of the array.
		right (int): The ending index of the second sorted portion of the array.

    Yields:
    	tuple: A tuple consisting of the current state of the array, the current indices of the left and right portions being merged, and the left and right indices of the original array being merged.
    """

	left_arr_size  = mid - left + 1
	right_arr_size = right - mid
	left_arr, right_arr = [], []
	
	for i in range(left_arr_size) : left_arr.append(arr[left + i])
	for i in range(right_arr_size): right_arr.append(arr[mid + i + 1])
	    
	k, i, j = left, 0, 0
	while i < left_arr_size and j < right_arr_size:
	    yield arr, left + i, mid + j, left, right
	
	    if left_arr[i] <= right_arr[j]:
	        arr[k] = left_arr[i]
	        i += 1
		
	    else: 
	        arr[k] = right_arr[j]
	        j += 1
	    k += 1
	 
	while i < left_arr_size:
	    arr[k] = left_arr[i]
	    i += 1
	    k += 1
	
	while j < right_arr_size:
	    arr[k] = right_arr[j]
	    j += 1
	    k += 1

def timSort(arr, beginning, ending):
	"""
    Sorts the array using the timsort algorithm.

    Timsort is a hybrid sorting algorithm derived from merge sort and insertion sort algorithms. 
    It uses insertion sort to sort small chunks of the array and then merges them using the 
    merge function. The algorithm works as follows:
    
    1. Calculate the minimum run size
    2. Sort the array in runs of size min_run using binary insertion sort
    3. Merge adjacent runs using the merge function until the array is completely sorted

    Args:
		arr: The array to be sorted
		beginning: The starting index of the array
		ending: The ending index of the array

    Yields:
		Generator object that yields a tuple (arr, i, j, left, right), where:
			arr: The array being sorted
			i: The index of the last element in the sorted range
			j: The index of the first element in the unsorted range
			left: The leftmost index of the range being merged
			right: The rightmost index of the range being merged

    """
	arr_len = len(arr) 
	min_run = calculate_min_run(arr_len)
	
	for start in range(0, arr_len, min_run): 
		end = min(start + min_run - 1, arr_len - 1) 
		yield from binaryinsertionSort(arr, start, end)
		
	size = min_run
	while size < arr_len: 
		for left in range(0, arr_len, 2 * size): 
			mid   = min(arr_len - 1, left + size - 1) 
			right = min(left + 2 * size - 1, arr_len - 1)
			yield from merge(arr, left, mid, right)
		size *= 2
		
