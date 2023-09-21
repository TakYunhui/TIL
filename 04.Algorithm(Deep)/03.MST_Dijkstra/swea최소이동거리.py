def dijkstra():
    # 비교 대상이 될 가중치 정보
    dist = [E * 100] * (V+1)
    visited = [0] * (V+1)
    # 시작지점은 항상 0 (해당 문제)
    dist[0] = 0

    for _ in range(V):
        next = 0
        min_v = E * 100

        # 최솟값 찾기
        for i in range(V+1):
            if not visited[i] and min_v > dist[i]:
                min_v = dist[i]
                next = i # 다음 조사 대상을 i로 갱신
        visited[next] = 1
        # 모든 노드에 대해서 도착할 수 있는 최소 가중치 갱신
        for j in range(V+1):
            if not visited[j] and dist[j] > dist[next] + arr[next][i]:
                dist[j] = dist[next] + arr[next][j]
    # 가중치 중 끝번(N번) 노드에 저장된 가중치
    return dist[V]

t = int(input())
for _ in range(t):
    V, E = map(int, input().split())
    arr = [[E * 100] * (V+1) for _ in range(V+1)]

    for i in range(E):
        S, E, W = map(int, input().split())
        arr[S][E] = W
    print(dijkstra())

