# 이진트리
import sys
sys.stdin = open('input.txt')


# 전위순회 VLR
# vortex 찍는 순간, 가지고 있는 값 바로 출력
# node: 현재 번호
def preorder(node):
    # node가 0이 아닐 때만 조사
    if node != 0:
        print(node, end=' ')
        # 자기 자신 출력 후, 다시 전위 순회 시작
        preorder(left[node])
        preorder(right[node])


# 중위순회 LVR
def inorder(node):
    if node != 0:
        inorder(left[node])
        print(node, end=' ')
        inorder(right[node])


# 후위순회 LRV
def postorder(node):
    if node != 0:
        postorder(left[node])
        postorder(right[node])
        print(node, end=' ')


v = int(input())
e = v - 1
edge = list(map(int, input().split()))

# 왼쪽 자식, 오른쪽 자식, 부모 정보
# 최대 정점 번호까지 들어가도록 v + 1 (인덱스 & 선수번호의 차)
left = [0] * (v+1)
right = [0] * (v+1)
parent = [0] * (v+1)
# [왼쪽, 오른쪽, 부모]
tree = [[0] * 3 for _ in range(v+1)]


# 간선 정보 전수 조사
# 간선 정보가 정렬되어있다면 그냥 왼쪽, 오른쪽 넣으면 됨
# 문제에 따라 정렬이 보장되지 않을 수 있음! 정렬 후 넣으셈
# how? 간선정보들을 묶어 넣고, sorted(function) 또는 sort(list method) 이용
for i in range(e):
    p, c = edge[i*2], edge[i*2+1]
    # 이진트리일 때만 가능한 방법 -> 자식이 최대 2개인 게 확정이니까!
    if left[p] == 0: # 아직 왼쪽 자식 기록 x
        left[p] = c
    else:
        right[p] = c
    # 부모 정보 넣기
    parent[c] = p

    if tree[p][0] == 0:
        tree[p][0] = c
    else:
        tree[p][1] = c
    tree[c][2] = p
print(tree)

# 부모루트 찾기
# root = 0
# for i in range(1, v+1):
#     if parent[i] == 0:
#         root = i
#         break
# print(root)

print('----전위 순회----')
preorder(1)
print()
print('----후위 순회----')
inorder(1)
print()
print('----중위 순회----')
postorder(1)