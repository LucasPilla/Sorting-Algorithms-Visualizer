def compAndSwap(a, i, j, dire):
    if (dire == 1 and a[i] > a[j]) or (dire == 0 and a[i] < a[j]):
        a[i], a[j] = a[j], a[i]

def bitonicMerge(a, low, cnt, dire):      # The sequence to be sorted starts at index position low
    if cnt > 1:
        k = int(cnt / 2)
        for i in range(low, low + k):
            compAndSwap(a, i, i + k, dire)
        bitonicMerge(a, low, k, dire)
        bitonicMerge(a, low + k, k, dire)


 
def bitonicSort(a, low, cnt, dire):             # sorting its two halves in opposite sorting orders
    if cnt > 1:
        k = int(cnt / 2)
        bitonicSort(a, low, k, 1)
        bitonicSort(a, low + k, k, 0)
        bitonicMerge(a, low, cnt, dire)




def sort(a, N, up):             # in ASCENDING order
    bitonicSort(a, 0, N, up)


a = []
print("How many numbers u want to enter?");
n = int(input())
print("Input the numbers:");
for i in range(n):
    a.append(int(input()))
up = 1

sort(a, n, up)
print("\n\nSorted array is:")
for i in range(n):
    print("%d" % a[i])
