# 비트 연산 사용
# T = int(input())
# numbers = list(range(1, 13))
#
# for tc in range(1, T+1):
#     N, K = map(int, input().split())
#     for x in range(1 << 12): # 12가 2의 승 수로 들어감 -> 4096
#         total = 0
#         count = 0
#         for y in range(12):
#             if x & (1 << y): # 조건 결과가 0이 아니라면
#                 total += numbers[y]
#                 count += 1
#
#         if (total == sum) and (count == N):
#             total += 1
#         print(count)