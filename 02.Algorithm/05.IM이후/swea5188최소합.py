'''
3
3
1 2 3
2 3 4
3 4 5
4
2 4 1 3
1 1 7 1
9 1 7 10
5 7 2 4
5
6 7 1 10 2
10 2 7 5 9
9 3 2 9 6
1 6 8 2 9
8 3 8 2 1
'''
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    case = [list(map(int, input().split())) for _ in range(n)]

