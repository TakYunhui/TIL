numbers = [-7, -3, -2, 5, 8]
N = 5

# numbers로 만들 수 있는 모든 경우의 수
# 1 << 2 == 2 ** N
# 1 왼쪽으로 3 번 쉬프트
# 0001 -> 1000
for x in range(1<<N): # x : 0~31(2진수로)  00001
    result = 0
    for y in range(N): # y : 0~4(10진수로) 00001
        if x & (1 << y):
            result += numbers[y]
    if result == 0:
        print(1)
        break

        # 그 모든 경우의 수에서,
        # numbers의 y번째 요소가
        # x번 경우의 수에 사용되었는지를 판별
        # x번 경우의 수가 1일때 bit -> 0001
        # numbers의 y번째 요소(0번째 요소) -> (1 << y)
        # numbers의 0번째 요소가 0001 -> (1 << 0)
        # numbers의 1번째 요소가 0010 -> (1 << 1)