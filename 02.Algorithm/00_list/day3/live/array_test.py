N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
total1 = 0
for i in range(N):
    total1 += arr[i][i]
    