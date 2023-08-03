# 특별한 정렬
# N개의 정수
# 가장 큰 수, 가장 작은 수, 2번째 큰 수, 2번째 작은 수
# 1 2 3 4 5 6 7 8 9 10
# 10 1 9 2 8 3 7 4 6 5

# 배열을 오름차순으로 정리 후
# 가장 뒤의 수, 가장 앞의 수 순서로 새 배열에 넣는다?

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    numbers.sort()
    big_numbers = numbers[(N//2):].sort(reverse=True)
    small_numbers = numbers[:(N//2)]
    new_numbers = [0 for _ in range(N)]

