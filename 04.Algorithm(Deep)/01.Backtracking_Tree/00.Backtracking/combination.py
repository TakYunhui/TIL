# nCr : n개의 요소 중 r개로 만들 수 있는 조합
# r : 현재 사용한 원소의 개수
# idx : 이번 회차 조사 시작 시점
def combination(r, idx):
    # 종료 시점
    if r == 3:
        print(completed_comb)
        return
    else:
        # for문 -> iterable한 요소의 길이 만큼 모두 순회
        #  range(s, e, default) -> s부터 e까지 1씩 증가
        # arr의 항상 0번째부터 N-1번째까지의 순으로 작성
        for i in range(idx, N):
            completed_comb[r] = arr[i]
            combination(r + 1, i + 1)


arr = [1, 2, 3, 4, 5]
N = len(arr)
# 완성된 조합 리스트
completed_comb = [0] * N
combination(0, 0)

print('--중복 조합--')
# 중복 조합
def combination2(r, idx):
    # 종료 시점
    if r == 3:
        print(completed_comb2)
        return
    else:
        # for문 -> iterable한 요소의 길이 만큼 모두 순회
        #  range(s, e, default) -> s부터 e까지 1씩 증가
        # arr의 항상 0번째부터 N-1번째까지의 순으로 작성
        for i in range(idx, N):
            completed_comb2[r] = arr[i]
            combination2(r + 1, i )

completed_comb2 = [0] * N
combination2(0, 0)