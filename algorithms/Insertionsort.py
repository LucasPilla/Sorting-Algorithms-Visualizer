def swap(l, i, j):
    temp = l[i]
    l[i] = l[j]
    l[j] = temp
 
l = list(map(int,input().split(" ")))
i = 0
while(i < len(l)):
    for j in range(i+1, len(l)):
        if(l[i] > l[j]):
            swap(l, i, j)
    i+=1
print("sorted list", l)
