from display import handleDrawing
def calculate_min_run(n): 
	last_bit = 0
	RUN_LEN = 32
	while n >= RUN_LEN: 
		last_bit |= n & 1
		n >>= 1
	return n + last_bit 

def insertion_sort(arr, start, end): 
	for i in range(start+1, end+1): 
		j = i 
		while j > start and arr[j] < arr[j - 1]:
			handleDrawing(arr, i, -1, j, -1)
			arr[j], arr[j - 1] = arr[j - 1], arr[j] 
			j -= 1

def merge(arr, left, mid, right):
	left_arr_size = mid - left + 1
	right_arr_size = right - mid
	left_arr, right_arr = [], []
	
	for i in range(0, left_arr_size):
	    left_arr.append(arr[left+i])
	for i in range(0, right_arr_size):
	    right_arr.append(arr[mid+1+i])
	    
	k = left
	i, j = 0, 0
	while i < left_arr_size and j < right_arr_size:
	    handleDrawing(arr, left+i, mid+j, left, right)
	    if left_arr[i] <= right_arr[j]:
	        arr[k] = left_arr[i]
	        i += 1
	    else: 
	        arr[k] = right_arr[j]
	        j+=1
	    k += 1
	 
	while i < left_arr_size:
	    arr[k] = left_arr[i]
	    i+=1
	    k+=1
	
	while j < right_arr_size:
	    arr[k] = right_arr[j]
	    j+=1
	    k+=1

def timSort(arr, beginning, ending): 
	arr_len = len(arr) 
	min_run = calculate_min_run(arr_len)
	for start in range(0, arr_len, min_run): 
		end = min(start + min_run - 1, arr_len - 1) 
		insertion_sort(arr, start, end) 
	size = min_run 
	while size < arr_len: 
		for left in range(0, arr_len, 2 * size): 
			mid = min(arr_len - 1, left + size - 1) 
			right = min(left + 2 * size - 1, arr_len - 1)
			merge(arr, left, mid, right)
		size = 2 * size