cal = '2+3*4/5'

result = ''

stack = []

# 전수조사
for char in cal:
    # 연산자라면
    if char in '+-/*()':
        if char == '(':
            stack.append(char)
        elif char in '*/':
            while stack and stack[-1] in '*/':
                result += stack.pop()
            stack.append(char)
        elif char in '+-':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.append(char)
        elif char in ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()
    else:
        # 정수면 result에 더해버린다
        result += char
    print(result, stack)
    while stack:
        result += stack.pop()
print(result, stack)