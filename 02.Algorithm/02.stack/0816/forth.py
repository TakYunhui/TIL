# 5일차 forth
# 예외를 위로 가게 하는 편이 낫다
t = int(input())
for tc in range(1, t+1):
    case = list(input().split())
    stack = []
    result = 0
    for c in case:
        if c not in '+-/*.':
            stack.append(int(c))
        elif c == '.':
            if len(stack) == 1:
                result = stack[-1]
            else:
                result = 'error'
        elif len(stack) >= 2:
            try:
                right = stack.pop()
                left = stack.pop()
            except IndexError:
                result = 'error'
            if c == '+':
                stack.append(left + right)
            elif c == '-':

                stack.append(left - right)
            elif c == '*':

                stack.append(left * right)
            elif c == '/':

                stack.append(left // right)
        elif len(stack) == 1 and c in '+-*/':
            result = 'error'
            break



    print(f'#{tc} {result}')







