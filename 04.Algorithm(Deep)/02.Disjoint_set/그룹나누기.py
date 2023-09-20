# 대표자가 같은지 찾는 함수 == 서로 같은 집합인지 판별
def find_set(x):
    if parent[x] == x:
        return x
    return find_set(parent[x])

# 대표자를 같게 만드는 함수 == 집합을 통합하는 역할
def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x == y:
        return 1
    # 더 작은 수를 대표자로 지정
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


t = int(input())
for tc in range(1, t+1):
    # n명의 사람, 번호 쌍의 개수 m
    n, m = map(int, input().split())
    parent = [i for i in range(n+1)]

    # 번호 m쌍 저장
    data = list(map(int, input().split()))
    # 2개씩 번호를 통합
    for i in range(0, len(data)-1, 2):
        a, b = data[i], data[i+1]
        union(a, b)

    result = set() # 중복 숫자 제거
    for i in range(1, n+1):
        result.add(find_set(i))

    print(f'#{tc} {len(result)}')