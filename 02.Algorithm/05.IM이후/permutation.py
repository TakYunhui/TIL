# now: 현재 조사 위치
# r: 최대 조사 대상 수
def perm(now, r):
    if now == r:
        print(check)
        return
    else:
        # 완전 검색
        for i in range(len(num)):
            # 중복 있는 순열은 visited 이 조건식 제거
            if visitied[i]:
                continue
            visitied[i] = True # i 번째 요소 사용?
            # 실제 사용 여부는 check에 표기
            check[now] = num[i]
            perm(now + 1, r)
            visitied[i] = False

# 반복에 대한 이해
# 브루트포스
# 재귀함수에 대한 이해
num = [1, 2, 3]
# 각 요소의 사용여부
visitied = [0] * len(num)
# 실제 순열에 구성되는 요소들을 담을 리스트
check = [0] * len(num)

perm(0, len(num))
