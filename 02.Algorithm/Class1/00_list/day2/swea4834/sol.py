# 0 ~ 9까지 N장의 카드
# 가장 많은 카드에 적힌 숫자와 카드의 장수 출력
# 카드 장수가 같을 때, 적힌 숫자가 큰 쪽을 출력

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = list(input())