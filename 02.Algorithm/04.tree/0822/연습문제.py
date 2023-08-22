# 중위 순회
# 완전 이진 트리 형식, 노드당 하나의 문자만 저장 -> 루트 1
# 필요한 크기의 배열 만들어서 저장
# 저장할 모양 결정하기

def inorder(p, n): # n 완전이진트리의 마지막 정점
    if p <= n:
        inorder(p * 2, n)      # 왼쪽 자식으로 이동
        print(tree[p], end='')  # 중위순회에서 할 일
        inorder(p * 2 + 1, n)  # 오른쪽 자식으로 이동
for tc in range(1, 11): # 10개의 테스트 케이스 고정
    n = int(input())
    tree = [0] * (n+1) # n번 노드까지 있는 완전이진트리
    for _ in range(n):
        arr = list(input().split())
        # tree[1] -> 'W'
        # '1' 'W' '2' '3'에서 앞의 두 정보만 활용(완전이진트리 특징)
        tree[int(arr[0])] = arr[1]
    # 중위순회
    print(f'#{tc} ', end='')
    inorder(1, n)      # root = 1
    print()

