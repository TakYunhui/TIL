v, e = map(int, input().split())
edge = []
for _ in range(e):
    f, t, w = map(int, input().split())
    edge.append([f, t, w])
# w 를 기준으로 정렬
edge.sort(key=lambda x: x[2])

# 사이클 발생 여부를 union find 로 해결
parents = [i for i in range(v)]

def find_set(x):
    if parents[x] == x:
        return  x
    return  find_set(parents[x])


def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x == y:
        return

    if x < y:
        parents[y] = x
    else:
        parents[x] = y

# 현재 방문한 정점 수
cnt = 0
sum_weight = 0
# edge를 정렬했기에 선택할 때 가장 적은 수부터 고르게 된다
for f, t, w in edge:
    # 싸이클이 발생하지 않는다면 == 두 개의 대표자가 서로 다르다면
    if find_set(f) != find_set(t):
        cnt += 1
        sum_weight += w
        union(f, t) # 같은 집합으로 묶어준다 (연결)
        # MST 구성이 끝나면
        if cnt == v:
            break

print(f'최소 비용 = {sum_weight}')