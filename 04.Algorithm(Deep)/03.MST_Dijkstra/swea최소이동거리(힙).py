import heapq
def dijkstra():
    # 우선순위 큐, 누적거리 저장할 배열 distance 이용
    INF = int(1e9) # 1억
    distance = [INF] * (n+1)
    pq = []
    heapq.heappush(pq, (0, 0))
    # 시작점 누적 거리의 합 0으로 지정
    distance[0] = 0

    while pq:
        # 현 시점에서 누적 거리가 가장 짧은 노드 꺼내기
        dist, now = heapq.heappop(pq)
        # 현재 보고있는 지점보다 더 짧게 방문한 적이 있다면 pass (변화 x)
        if distance[now] < dist:
            continue

        # 인접 노드 확인
        for next in arr[now]:
            next_node = next[0]
            cost = next[1]

            # next_node로 가기위한 누적 거리
            new_cost = dist + cost

            # 누적 거리가 기존보다 크다면 이용하지 않을 것이므로 pass
            if distance[next_node] <= new_cost:
                continue

            # 계산한 누적 거리가 더 작다면(짧다면) 바꿔준다
            distance[next_node] = new_cost
            heapq.heappush(pq, (new_cost, next_node))

    return distance[n]

t = int(input())
for tc in range(1, t+1):
    n, e = map(int, input().split()) # 마지막 정점 번호, 간선 개수
    arr = [[] for _ in range(n+1)]
    for _ in range(e):
        s, e, w = map(int, input().split()) # 시작, 끝, 거리 가중치
        arr[s].append((e, w))
    result = dijkstra()
    print(f'#{tc} {result}')