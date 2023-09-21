# 누적거리 + 누적거리 기준 idq(우선순위 큐) 구현
# 갈 수 있는 경로 중 누적거리가 가장 짧은 것부터 선택
'''
6 8
0 1 2
0 2 4
1 2 1
1 3 7
2 4 3
3 4 2
3 5 1
4 5 5
'''
import heapq

n, m = map(int, input().split())
# 인접리스트
graph = [[] for _ in range(n)]
for _ in range(m):
    f, t, w = map(int, input().split())
    graph[f].append([t, w])

# 누적거리 계속 저장할 배열
INF = int(1e9) # 최대값으로 1억
distance = [INF] * n

def dijkstra(start): # 시작점
    # 우선순위 큐
    pq = []
    heapq.heappush(pq, (0, start))
    distance[start] = 0 # 시작점 누적거리의 합을 0으로 지정

    while pq:
        # 현 시점에서 누적 거리가 가장 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(pq)

        # 이미 방문한 지점 + 누적 거리가 더 짧게 방문한 적이 있다면 pass
        if distance[now] < dist:
            continue

        # 인접 노드 확인
        for next in graph[now]:
            next_node = next[0]
            cost = next[1]

            # next_node 로 가기 위한 누적 거리
            new_cost = dist + cost

            # 누적 거리가 기존보다 크다면
            if distance[next_node] <= new_cost:
                continue

            # 누적 거리가 더 짧다면 바꿔줌
            distance[next_node] = new_cost
            heapq.heappush(pq, (new_cost, next_node))

dijkstra(0)
print(distance)