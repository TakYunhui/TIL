# 객체 대신 리스트로 만들기
N = 6
arr = [6, 3, 2, 7, 9, 1]

tree = [0] * (N+1)  # 0번 안쓸거임
last = 1

for i in range(N):
    if tree[i] == 0:
        tree[last] = arr[i]
    else:
        last += 1
        tree[last] = arr[i]
        child = last   # 자식의 위치
        # 완전이진트리에서 부모 위치 = 자식 위치 // 2
        parent = child // 2

        # 만약 부모의 값이 자식보다 크면
        # 최소힙을 만족할 수 없으니 두 값을 swap
        while parent >= 1 and tree[parent] > tree[child]:
            # 부모, 자식의 값 교환
            tree[parent], tree[child] = tree[child], tree[parent]
            # 자식 위치가 swap한 부모 위치가 되도록 설정
            child = parent
            # 부모의 값은?
            parent = child//2

    print(tree)