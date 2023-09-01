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
	"""
    for i in range(start, end + 1):
        val = array[i]
        j   = binary_search(array, val, start, i - 1, i)
        yield array, start, i-1, j, i
        array[0: len(array)] = array[: j] + [val] + array[j: i] + array[i + 1:]

def merge(arr, left, mid, right):
	"""
    This function merges two sorted portions of an array.
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
    Timsort first divides the input list into small 
	sub-lists called "runs" and sorts each run using Insertion Sort. 
	It then merges adjacent runs into larger runs until a complete sort is achieved. 
	The algorithm uses a combination of the best-case time complexity of Insertion Sort 
	and the worst-case time complexity of Merge Sort to achieve good performance on both 
	small and large lists.

	Time complexity: O(nlog²n).

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
		
