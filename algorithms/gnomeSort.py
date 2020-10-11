from display import handleDrawing

def gnomeSort(a, *args):
    i,j,size = 1,2,len(a)
    while i < size:
        if a[i-1] <= a[i]:
            i,j = j, j+1
        else:
            handleDrawing(a, i, i-1, 0, j+1)
            a[i-1],a[i] = a[i],a[i-1]
            i -= 1
            if i == 0:
                i,j = j, j+1
    return a
