import heapq
def prim(s):
    pq = []
    MST = [0] * (v+1)
    # 가중치(간선 간 거리), 정점 번호
    heapq.heappush(pq, (0, s))
    total = 0

    while pq:
        weight, node = heapq.heappop(pq)

        if MST[node]:
            continue

        MST[node] = 1
        total += weight

        for next in graph[node]:
            if MST[next[0]]:
                continue
            # push(가중치, 정점 번호)
            heapq.heappush(pq, (next[1], next[0]))
    return total

t = int(input())
for tc in range(1, t+1):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        n1, n2, w = map(int, input().split())
        graph[n1].append((n2, w))
        graph[n2].append((n1, w))


    print(f'#{tc} {prim(0)}')
