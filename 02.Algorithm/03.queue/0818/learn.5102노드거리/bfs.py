# v: 노드 개수, e: 방향성이 없는 간선
# 출발 노드 -> 도착 노드
# 최소 몇 개의 간선을 지나면???
# 노드는 1번부터 존재, 간선으로 연결되지 않은 경우도 있다
import sys
sys.stdin = open('sample_input.txt')

def bfs(v, s, g):
    visited = [0] * (v+1) # 방문 여부 생성
    q = [s]               # 큐 생성 후 시작지점 인큐
    visited[s] = 1        # 시작지점 방문
    while q:                # 큐가 비워질 때까지
        focus = q.pop(0)    # 큐에 가장 먼저 들어온 값 빼기(디큐)
        for near in range(v+1):
            if matrix[focus][near] == 1 and visited[near] == 0:
                q.append(near)
                visited[near] = visited[focus] + 1
                if near == g:
                    # print(near, visited[near])
                    return visited[near] -1
    return 0





# 테스트 케이스 개수
t = int(input())
for tc in range(1, t+1):
    # v, e
    v, e = map(int, input().split())

    data = []
    for i in range(e):
        n1, n2 = map(int, input().split())
        data.append(n1)
        data.append(n2)
    s, g = map(int, input().split())
    matrix = [[0] * (v+1) for _ in range(v+1)]

    for i in range(0, e*2, 2):
        matrix[data[i]][data[i+1]] = 1
        matrix[data[i+1]][data[i]] = 1
    # print(data, matrix)
    print(f'#{tc} {bfs(v, s, g)}')