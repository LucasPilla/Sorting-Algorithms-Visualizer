from display import handleDrawing

def gnomeSort(a, *args):
    i,size = 0,len(a)
    while i < size:
        if a[i-1] <= a[i] or i == 0:
             handleDrawing(a, i, i-1, -1, -1)
             i += 1
        else:
            handleDrawing(a, i, i-1, -1, -1)
            a[i-1],a[i] = a[i],a[i-1]
            i -= 1
