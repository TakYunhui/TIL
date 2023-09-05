# now : 현재 조사 위치
# r : 최대 조사 대상 수
# idx : 이번 회차 조사 시작 지점
def comb(now, r, idx):
    if now == r:
        print(check[:r])
    else:
        for i in range(idx, len(num)):
            check[now] = num[i]
            # 다음 번 조사 -> 다음 위치로
            # 중복 없는 조합: i + 1, 저 i는 빼주고 조사해주세요
            # 중복 있는 조합: i, 저도 넣어서 조사해주세요
            comb(now+1, r, i)

num = [1, 2, 3]
# 실제 조합에 구성되는 요소들을 담을 리스트
check = [0] * len(num)
comb(0, 2, 0)