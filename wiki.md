## Algorithms
### 1. Bubble Sort
Bubble sort is a comparison-based sorting algorithm in which each pair of adjacent elements is compared and the elements are swapped if they are not in order. 

Complexity:
| Best Case        | Average Case | Worst Case|          
| ------------- |:-------------:|:------------|
| O(n)      | O(n2) |O(n2)                      |
***

![bubble sort animated](http://www.xybernetics.com/techtalk/SortingAlgorithmsExplained/images/bubble1.gif) 

source: http://www.xybernetics.com/techtalk/SortingAlgorithmsExplained/SortingAlgorithmsExplained.html

### 2. Selection Sort
Selection sort is an in-place comparison-based algorithm in which the list is divided into two parts, the sorted part at the left end and the unsorted part at the right end. Initially, the sorted part is empty and the unsorted part is the entire list.

Complexity:
| Best Case        | Average Case | Worst Case|          
| ------------- |:-------------:|:------------|
| O(n2)      | O(n2) |O(n2)                      |

![selection sort animated](http://www.xybernetics.com/techtalk/SortingAlgorithmsExplained/images/SelectionEg01.gif)

source: http://www.xybernetics.com/techtalk/SortingAlgorithmsExplained/SortingAlgorithmsExplained.html

### 3. Insertion Sort
Insertion sort is an in-place comparison-based sorting algorithm. Here, a sub-list is maintained which is always sorted. For example, the lower part of an array is maintained to be sorted. An element which is to be 'insert'ed in this sorted sub-list, has to find its appropriate place and then it has to be inserted there. Hence the name, insertion sort. 

Complexity:
| Best Case        | Average Case | Worst Case|          
| ------------- |:-------------:|:------------|
| O(n)      | O(n2) |O(n2)                      |

![insertion sort animated](https://i.pinimg.com/originals/92/b0/34/92b034385c440e08bc8551c97df0a2e3.gif)

source: http://www.xybernetics.com/techtalk/SortingAlgorithmsExplained/SortingAlgorithmsExplained.html

### 4. Cocktail Sort
Cocktail Sort is a variation of Bubble sort. The Bubble sort algorithm always traverses elements from left and moves the largest element to its correct position in first iteration and second largest in second iteration and so on. Cocktail Sort traverses through a given array in both directions alternatively.This algorithm is not suitable for large data sets where n is the number of items but is faster than bubble sort.

Complexity:
| Best Case        | Average Case | Worst Case|          
| ------------- |:-------------:|:------------|
| O(1)      | O(n2) |O(n2)                      |

![cocktail sort animated](https://i.makeagif.com/media/11-26-2015/9SMe_Z.gif)
source: https://www.youtube.com/watch?v=Xmx_6YRBaq8


### 5. Merge Sort
Merge sort is a sorting technique based on divide and conquer technique. It is one of the most respected algorithms. Merge sort first divides the array into equal halves and then combines them in a sorted manner.

Complexity:
| Best Case        | Average Case | Worst Case|          
| ------------- |:-------------:|:------------|
| O(nlogn)      | O(nlogn) |O(nlogn)                      |

![merge sort animated](http://www.xybernetics.com/techtalk/SortingAlgorithmsExplained/images/merge.gif)

source: http://www.xybernetics.com/techtalk/SortingAlgorithmsExplained/SortingAlgorithmsExplained.html


### 6. Quick Sort
Quick sort is a highly efficient sorting algorithm and is based on partitioning of array of data into smaller arrays. A large array is partitioned into two arrays one of which holds values smaller than the specified value, say pivot, based on which the partition is made and another array holds values greater than the pivot value. Quicksort partitions an array and then calls itself recursively twice to sort the two resulting subarrays.

Complexity:
| Best Case        | Average Case | Worst Case|          
| ------------- |:-------------:|:------------|
| O(nlogn)      | O(nlogn) |O(n2)                      |

![quick sort animated](http://www.xybernetics.com/techtalk/SortingAlgorithmsExplained/images/quick1.gif)

source: http://www.xybernetics.com/techtalk/SortingAlgorithmsExplained/SortingAlgorithmsExplained.html


### 7. Counting Sort
Counting sort is a sorting technique based on keys between a specific range. It works by counting the number of objects having distinct key values (kind of hashing). Then doing some arithmetic to calculate the position of each object in the output sequence. 

Complexity:
| Best Case        | Average Case | Worst Case|          
| ------------- |:-------------:|:------------|
| O(n+k)      | O(n+k) |O(n+k)                      |

**Filling the count array:**

![count sort animated 1](https://3.bp.blogspot.com/-jJchly1BkTc/WLGqCFDdvCI/AAAAAAAAAHA/luljAlz2ptMndIZNH0KLTTuQMNsfzDeFQCLcB/s1600/CSortUpdatedStepI.gif)

source: https://nguyenvanhieu.vn/counting-sort/

**Actual sorting:**

![count sort animated 2](https://1.bp.blogspot.com/-xPqylngqASY/WLGq3p9n9vI/AAAAAAAAAHM/JHdtXAkJY8wYzDMBXxqarjmhpPhM0u8MACLcB/s1600/ResultArrayCS.gif)

source: https://nguyenvanhieu.vn/counting-sort/

### 8. Heap Sort
Heap sort is a comparison based sorting technique based on Binary Heap data structure. It is similar to selection sort where we first find the maximum element and place the maximum element at the end. We repeat the same process for the remaining elements. 

Complexity:
| Best Case        | Average Case | Worst Case|          
| ------------- |:-------------:|:------------|
| O(nlogn)      | O(nlogn) |O(nlogn)                      |

A Binary Heap is a Complete Binary Tree where items are stored in a special order such that value in a parent node is greater(or smaller) than the values in its two children nodes. The former is called as max heap and the latter is called min-heap. The heap can be represented by a binary tree or array.

![heap sort animated](http://www.xybernetics.com/techtalk/SortingAlgorithmsExplained/images/heap1.gif)

source: http://www.xybernetics.com/techtalk/SortingAlgorithmsExplained/SortingAlgorithmsExplained.html


### 9. Bucket Sort
Bucket sort is mainly useful when input is uniformly distributed over a range. It works by distributing the elements of an array into a number of buckets. Each bucket is then sorted individually, either using a different sorting algorithm, or by recursively applying the bucket sorting algorithm. 

Complexity:
| Best Case        | Average Case | Worst Case|          
| ------------- |:-------------:|:------------|
| O(n+k)      | O(n+k) |O(n2)                      |

![bucket sort animated](https://miro.medium.com/max/800/1*_2l-UN7jcQp54hgazT6iVA.gif)

source: https://medium.com/@allegranzia/bucket-sort-in-ruby-a062d60ca4b3
