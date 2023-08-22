import sys
sys.stdin = open('input (1).txt')


def inorder(n):
    if n:
        # 아래 방식은 완전이진트리만 가능
        # inorder(n*2)
        # inorder(n * 2 + 1)

        # 자식 관계 불러오기
        inorder(ch1[n])
        inorder(ch2[n])
        if tree[n] in '+-*/':  # 연산자면 계산,
            if len(tmp) >= 2:  # tmp 리스트 안에 요소가 2개 이상일 때만 실행
                right = tmp.pop()
                left = tmp.pop()
                if tree[n] == '+':
                    tmp.append(left + right)
                elif tree[n] == '-':
                    tmp.append(left - right)
                elif tree[n] == '/':
                    tmp.append(left // right)
                elif tree[n] == '*':
                    tmp.append(left * right)
            # 피연산자면 정수형변환해서 tmp에 넣는다
        else:
            tmp.append(int(tree[n]))
    return tmp


for tc in range(1, 11):
    n = int(input())  # 정점개수
    # tree: 전체 노드가 1부터 순번대로 들어감
    # ch1, ch2:  부모 - 자식 관계 나타내는 리스트
    # ch1이 왼쪽 자식, ch2가 오른쪽 자식
    tree = [0] * (n + 1)
    # 이진 트리 리스트로 만들기
    ch1 = [0] * (n + 1)
    ch2 = [0] * (n + 1)
    for i in range(n):
        arr = input().split()
        # print(arr)
        if arr[1] in '+-*/':
            p, c, c2 = int(arr[0]), int(arr[2]), int(arr[3])
            ch1[p] = c
            ch2[p] = c2
        tree[int(arr[0])] = arr[1]

    tmp = []
    print(f'#{tc}', inorder(1)[0])

    # ch1 = [0] * (n+1)
    # ch2 = [0] * (n+1)
    # for i in range(n):
    #     if arr[i][1] in '+-*/':
    #         p, c, c2 = int(arr[i][0]), int(arr[i][2]), int(arr[i][3])
    #         ch1[p] = c
    #         ch2[p] = c2
    #     else:
    #         p, c = int(arr[i][0]), int(arr[i][1])
    #         print(p, c)
    #         if ch1[p] == 0:
    #             ch1[p] = c
    #         else:
    #             ch2[p] = c
    # print(ch1, ch2)
