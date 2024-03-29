class Node: 
    def __init__(self , item): 
        self.key = item 
        self.left = None
        self.right = None
        
def preorder(root): 
    if root is not None: 
        print (root.key,end=' ') 
        preorder(root.left) 
        preorder(root.right)
        
def getTrees(arr,start,end):
    trees = [] 
    if start > end : 
        trees.append(None) 
        return trees 
    for i in range(start , end+1):
        ltrees = getTrees(arr , start , i-1) 
        rtrees = getTrees(arr , i+1 , end)
        for j in ltrees : 
            for k in rtrees :
                node = Node(arr[i])
                node.left = j
                node.right = k
                trees.append(node) 
    return trees

inp = [int(x) for x in input().split()]
n = len(inp) 
trees = getTrees(inp,0,n-1) 
print("Preorder traversals :")
for i in trees : 
    preorder(i)
    print()
