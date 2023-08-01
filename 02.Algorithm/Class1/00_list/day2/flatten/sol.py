# flatten
import  sys
sys.stdin = open('input (3).txt')
T = 10
for tc in (1, T+1):
    N = int(input())
    heights = list(map(int, input().split()))
    max_h = 0
    min_h = 100

    for height in heights:
        if height > max_h:
            max_h = height
        if height < min_h:
            min_h = height
        print(max_h, min_h)