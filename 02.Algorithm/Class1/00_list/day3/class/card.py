# N | 0 ~ 9
# 가장 많은 카드에 적힌 숫자 + 카드 장 수
# 카드 장수가 같을 때, 적힌 숫자가 큰 쪽 출력
# => 카운팅 배열 이용

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # ↓ 공백이 없어서 split()안 씀 !
    ai = list(map(int, input()))
    counting_arr = [0] * 10
    for num in ai:
        counting_arr[num] += 1
    result = 0
    num = 0
    for index in range(len(counting_arr)):
        if counting_arr[index] >= result:
            result = counting_arr[index]
            num = index
    print(f'#{tc} {num} {result}')
