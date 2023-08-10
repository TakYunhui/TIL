# DFS
# 간선 양방향 이동 X 일직선 이동
# 특정한 두 개의 노드에 경로가 존재하는지 확인
# 경로가 있으면 1, 없으면 0 출력
import sys
sys.stdin = open('sample_input.txt')

# 노드 경로 조사
def DFS(S, G):
    stack = []
    stack.append(S)
    visited = [False] * (V+1) # 방문 기록 체크
    while stack: # 스택에 조사할 값이 있는 동안
        start = stack.pop() # 후입선출 | 1부터...
        if visited[start] == 0: # 방문한 적 없다면
            visited[start] = True # 방문 체크
            # print(start, end=' ')
            for next in range(V+1): # 다음 위치 조사| 0 0 0 1 1 0 0
                # 현재 노드와 다음 노드 사이 에 간선이 있고,
                # 노드가 방문한 적 없다면
                if matrix[start][next] == 1 and visited[next] == 0:
                    if next == G: # 다음 노드가 목표 노드와 같다면
                        return 1  # 탐색 경로에서 목표에 도달 -> 경로 존재함
                    stack.append(next) # 다음 노드를 스택에 추가
    return 0
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    # 이동 가능한 정보 2차원 리스트
    matrix = [[0]*(V+1) for _ in range(V+1)]
    # E개의 줄에 걸쳐 간선 정보가 주어짐
    data = []
    for _ in range(E):
        d1, d2 = map(int, input().split())
        data.append(d1)
        data.append(d2)
    # 모든 간선 순회
    for i in range(0, E * 2, 2):  # 간선 0 1 | 1 2 < 두 개씩 자료로 주어지므로 이러한 범위 가짐
        matrix[data[i]][data[i + 1]] = 1
    '''
    for i in range(E):
        d1, d2 = map(int, input().split())
        matrix[d1][d2] = 1
    '''

    # E개의 줄 이후로 경로의 존재를 확인할 출발 노드 S와 도착 노드 G
    S, G = map(int, input().split())
    print(f'#{tc} {DFS(S,G)}')
