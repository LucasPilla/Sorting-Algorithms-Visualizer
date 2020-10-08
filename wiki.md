## Algorithms
### 1. Bubble Sort
Bubble sort is a comparison-based sorting algorithm in which each pair of adjacent elements is compared and the elements are swapped if they are not in order. This algorithm is not suitable for large data sets as its average and worst case complexity are of Ο(n2) where n is the number of items
![bubble sort animated](https://media.giphy.com/media/oz7ZqxKxBP1GCHjVA8/giphy.gif) 


### 2. Selection Sort
Selection sort is an in-place comparison-based algorithm in which the list is divided into two parts, the sorted part at the left end and the unsorted part at the right end. Initially, the sorted part is empty and the unsorted part is the entire list.This algorithm is not suitable for large data sets as its average and worst case complexity are of Ο(n2) where n is the number of items.

![selection sort animated](https://miro.medium.com/max/1400/1*5WXRN62ddiM_Gcf4GDdCZg.gif)

### 3. Insertion Sort
Insertion sort is an in-place comparison-based sorting algorithm. Here, a sub-list is maintained which is always sorted. For example, the lower part of an array is maintained to be sorted. An element which is to be 'insert'ed in this sorted sub-list, has to find its appropriate place and then it has to be inserted there. Hence the name, insertion sort. This algorithm is not suitable for large data sets as its average and worst case complexity are of Ο(n2) where n is the number of items.
![insertion sort animated](https://i.pinimg.com/originals/92/b0/34/92b034385c440e08bc8551c97df0a2e3.gif)


### 4. Cocktail Sort
Cocktail Sort is a variation of Bubble sort. The Bubble sort algorithm always traverses elements from left and moves the largest element to its correct position in first iteration and second largest in second iteration and so on. Cocktail Sort traverses through a given array in both directions alternatively.This algorithm is not suitable for large data sets as its average and worst case complexity are of Ο(n2) where n is the number of items but is faster than bubble sort.
![cocktail sort animated](https://i.makeagif.com/media/11-26-2015/9SMe_Z.gif)

### 5. Merge Sort
Merge sort is a sorting technique based on divide and conquer technique. With worst-case time complexity being Ο(n log n), it is one of the most respected algorithms. Merge sort first divides the array into equal halves and then combines them in a sorted manner.

![merge sort animated](https://gifimage.net/wp-content/uploads/2018/11/mergesort-gif-5.gif)

### 6. Quick Sort
Quick sort is a highly efficient sorting algorithm and is based on partitioning of array of data into smaller arrays. A large array is partitioned into two arrays one of which holds values smaller than the specified value, say pivot, based on which the partition is made and another array holds values greater than the pivot value. Quicksort partitions an array and then calls itself recursively twice to sort the two resulting subarrays. This algorithm is quite efficient for large-sized data sets as its average and worst-case complexity are O(nLogn).

![quick sort animated](https://thumbs.gfycat.com/PleasantCloseEyelashpitviper-size_restricted.gif)

### 7. Counting Sort
Counting sort is a sorting technique based on keys between a specific range. It works by counting the number of objects having distinct key values (kind of hashing). Then doing some arithmetic to calculate the position of each object in the output sequence. Time Complexity is  O(n+k) where n is the number of elements in input array and k is the range of input.

**Filling the count array:**

![count sort animated 1](https://3.bp.blogspot.com/-jJchly1BkTc/WLGqCFDdvCI/AAAAAAAAAHA/luljAlz2ptMndIZNH0KLTTuQMNsfzDeFQCLcB/s1600/CSortUpdatedStepI.gif)

**Actual sorting:**

![count sort animated 2](https://1.bp.blogspot.com/-xPqylngqASY/WLGq3p9n9vI/AAAAAAAAAHM/JHdtXAkJY8wYzDMBXxqarjmhpPhM0u8MACLcB/s1600/ResultArrayCS.gif)

### 8. Heap Sort
Heap sort is a comparison based sorting technique based on Binary Heap data structure. It is similar to selection sort where we first find the maximum element and place the maximum element at the end. We repeat the same process for the remaining elements. Time complexity of Heap Sort is O(nLogn).

A Binary Heap is a Complete Binary Tree where items are stored in a special order such that value in a parent node is greater(or smaller) than the values in its two children nodes. The former is called as max heap and the latter is called min-heap. The heap can be represented by a binary tree or array.

![heap sort animated](https://www.codesdope.com/staticroot/images/algorithm/heapsort2.gif)

### 9. Bucket Sort
Bucket sort is mainly useful when input is uniformly distributed over a range. It works by distributing the elements of an array into a number of buckets. Each bucket is then sorted individually, either using a different sorting algorithm, or by recursively applying the bucket sorting algorithm. Time complexity is O(n).

![bucket sort animated](https://miro.medium.com/max/800/1*_2l-UN7jcQp54hgazT6iVA.gif)

