# 순열
# nPr : n개의 요소 중 r 개를 사용하여 순열
# r : 내가 사용하고 있는 값의 수
def perm(r):
    # 재귀 함수
    # 기저 조건

    if r == N:
        # 내가 원하는 무언가를 실행
        print(completed_perm)
        return
    else:
        # 내가 가진 arr의 모든 원소를 매번 사용할 것인지 체크
        for i in range(N):
            # arr의 i번째 요소를 쓴 적이 있는지 없는지를 기준으로 판단
            # if visited[i] == True: # i번째 값을 채웠다
            if not visited[i]: # i번째를 아직 쓰지 않았다면
                visited[i] = True
                # r : 사용한 수의 개수 -> 0번째 위치에 값을 담으면 r 1 증가
                # arr의 i번째
                completed_perm[r] = arr[i]
                perm(r + 1) # 다음 번 조사에는 하나 채웠다
                visited[i] = False


arr = [1, 2, 3]
N = len(arr)
# 내가 perm 함수 호출 시 arr의 i번째 값을 썼었던 적이 있는지 판별별
visited = [0] * N
completed_perm = [0] * N
perm(0)

print('-- 중복 순열 --')
# 중복순열
# nPr : n개의 요소 중 r 개를 사용하여 순열
# r : 내가 사용하고 있는 값의 수
def perm2(r, K):
    if r == K:
        print(completed_perm)
        return
    else:
        for i in range(N):
            completed_perm[r] = arr[i]
            perm2(r + 1, K)

completed_perm = [0] * N
perm2(0, 2)