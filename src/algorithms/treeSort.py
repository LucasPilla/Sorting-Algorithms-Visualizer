class Node:
    def __init__(self,val):
      self.val = val
      self.left = None
      self.right = None

def insertNode(root, val):
    #if root is empty define it
    if root is None:
        return Node(val)
    else:
        #print(root.val, val)
        if root.val > val:
            
            #if the value is less than root insert on the left
            root.left = insertNode(root.left, val)
        elif root.val <= val:
            #>= insert on the right
            root.right = insertNode(root.right, val)
    return root




def inorderArr(root, arr):
    #retireve an array of the inorder tree
    if root != None:
        arr = inorderArr(root.left, arr)
        arr.append(root.val)
        arr = inorderArr(root.right, arr)
    return arr

def treeSort(array):
    root = None
    #insert unordered array into BST
    for i in array:
        root = insertNode(root, i)
    return inorderArr(root, [])

#
# def main():
#     a = [1,5,6,9,10,2,8,4,7,3]
#     print (treeSort(a))

# if __name__ == "__main__":
#     main()
