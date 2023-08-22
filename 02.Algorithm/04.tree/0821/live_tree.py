# 전위순회 VLR
def preorder(T):
    if T: # T is not None
        visit(T)
        preorder(T.left)
        preorder(T.right)

# 중위순회 LVR
def inorder(T):
    if T:
        inorder(T.left)
        visit(T)
        inorder(T.right)

# 후위순회 LRV
def postorder(T):
    if T:
        postorder(T.left)
        postorder(T.right)
        visit(T)