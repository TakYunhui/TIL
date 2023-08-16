for tc in range(1, 11):
    n = int(input())
    case = input()
    susik = ''
    stack = []
    icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1}
    # “3+4+5*6+7”
    # "34+56*+7+"
    for c in case:
        if c in '+*':
            if stack and icp[c] <= icp[stack[-1]]:
                # 스택에 값이 있고, 현재 보고 있는 값보다 우선 순위가 낮은 것을 발견할 때까지
                while stack and icp[c] <= icp[stack[-1]]:
                    susik += stack.pop()
                stack.append(c)
            elif stack and icp[c] > icp[stack[-1]]:
                stack.append(c)
            else:
                stack.append(c)
        else:
            susik += c
    while stack:
        susik += stack.pop()


    stack = []
    for x in susik:
        if x in '+*':
            right = stack.pop()
            left = stack.pop()
            if x == '+':
                stack.append(left + right)
            elif x == '*':
                stack.append(left * right)
        else:
            stack.append(int(x))

    print(f'#{tc} {stack[-1]}')