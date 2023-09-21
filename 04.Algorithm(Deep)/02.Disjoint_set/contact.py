from collections import deque
def bfs(start):
    global last
    q = deque([start])
    visited[start] = 1

    while q:
        start = q.popleft()
        for node in graph[start]:
            if visited[node]:
                continue
            visited[node] = visited[start] + 1
            q.append(node)
            # 가장 마지막 단계의 숫자가 last에 저장될 것
            if visited[node] >= last:
                last = visited[node]
    return last



for tc in range(1, 11):
    # 입력 받는 데이터 길이 n 과 시작점 start
    n, start = map(int, input().split())
    data = list(map(int, input().split()))
    # 100까지의 번호가 나오므로 100번까지 들어가도록 101로 range 설정
    graph = [[] for _ in range(101)]
    # 주어진 data에서 숫자 2개씩 가져와서 인접리스트 생성
    for i in range(0, n, 2):
        a, b = data[i], data[i+1]
        graph[a].append(b)
    # 방문 체크 리스트 함수 밖에서도 쓸거니까 함수 외부에 위치
    visited = [0] * (101)
    result = 0
    last = 0
    # bfs 실행
    bfs(start)
    # 가장 마지막 단계의 것 중 가장 큰 숫자를 저장할 것
    # 마지막에 연락할 값들을 계속 값을 덮어씌우며 저장하는 것과 마찬가지인데 가장 큰 값이 결과에 들어가게 된다
    for j in range(101):
        if visited[j] == last:
            result = j

    print(f'#{tc} {result}')