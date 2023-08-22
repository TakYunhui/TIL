# binary search tree
# Tree Node를 하나의 객체로 만들어서 다루기
class TreeNode:
    def __init__(self, value):
        self.value = value
        # 노드가 하나면 왼쪽도 오른쪽도 없음
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return TreeNode(value)

    if value < root.value:
        # 바로 값을 할당하면 추후 들어올 값들에 대비할 수 없음
        # 재귀로 None과 value를 비교하게 하여 왼쪽에 값을 넣음
        root.left = insert(root.left, value)
    else: # 오른쪽도 마찬가지로 넣어준다
        root.right = insert(root.right, value)

    return root

def inorder(node):
    if node:
        inorder(node.left)
        print(node.value, end=' ')
        inorder(node.right)

# 정렬되지 않은 배열
arr = [13, 2, 8, 7, 9, 17, 6, 1]

root = TreeNode(arr[0])

for value in range(1, len(arr)):
    insert(root, value)

print(root.value)
print(root.left.value)

inorder(root)