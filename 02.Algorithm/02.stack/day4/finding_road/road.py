import sys
sys.stdin = open('input.txt')
# 출발점 0, 도착점 99
# 정점(노드)의 개수는 출발, 도착 제외 최대 98
def DFS(node):
    stack = [node]
    visited = [False] * (100)
    while stack: # stack에 값이 존재하는 동안
        start = stack.pop() # 후입선출
        if visited[start] == 0: # start에 방문한 적 없다면
            visited[start] = True # 방문 체크
            for next in range(100): # 인접 노드 조사
                #  start와 next 사이 간선이 있고, 방문한 적 없다면
                if matrix[start][next] == 1 and visited[next] == 0:
                    if next == 99:
                        return 1
                    stack.append(next) # next 노드 번호를 스택에 추가 (이동)
    return 0

for _ in range(10):
    tc, E = map(int, input().split())
    data = list(map(int, input().split()))
    matrix = [[0]*(100) for _ in range(100)]
    # print(data)
    for i in range(0, E*2, 2): # 간선 데이터
        matrix[data[i]][data[i+1]] = 1
    # print(matrix)

    print(f'#{tc} {DFS(0)}')
