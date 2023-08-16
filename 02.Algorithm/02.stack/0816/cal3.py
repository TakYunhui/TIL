for tc in range(1, 11):
    # 필요 데이터 입력
    n = int(input())
    case = input()
    # 입력되는 토큰 우선순위, 스택 우선순위
    icp = {'(': 3, '*': 2, '+': 1}
    isp = {'(': 2, '*': 2, '+': 1}
    stack = []
    susik = ''


    print(susik)
    print(f'{tc}')