# babygin
'''
124783
667767
054060
101123
'''
# row : 현재 조사 대상
# chosen : 선택 대상
# 완전검색
# 모든 n개의 원소를 다 조사했는지 판단
def perm(row, chosen):
    if row == n:
        for i in chosen:
            print(data[i], end=' ')
        print()
        pass
    # 모든 n개의 원소 조사했는지 판단
    for i in range(n):
        # i번째에 쓰겠다고 이전에 판정된 적이 있다면,
        # 현재 조사 대상을 i번째에 쓸 수 없으므로
        if i in chosen:
            continue
        chosen[row] = i # row번째 대상을 i번째에 둬서 사용
        perm(row+1, chosen)
        chosen[row] = -1

for tc in range(1, 5):
    n = 6
    data = input()
    # i번째에 들어갈 수 있는 수 0, n-1 까지를 제외한
    chosen = [-1] * n
    perm(0, chosen)