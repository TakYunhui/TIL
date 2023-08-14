# 후위표기법 22p
stack = [0] * 100
top =  -1
susik = '6528-*2/+'
for x in susik:
    if x not in '+-/*': # 피연산자면 
        top += 1        # push(x)
        stack[top] = int(x)
    else:
        right = stack[top] # 최상단 꺼내기
        top -= 1
        left = stack[top] # 하나 꺼내고 그 다음 최상단 꺼내기
        top -= 1

        if x == '+': # 먼저 꺼낸 것이 오른쪽으로 감 
            # 계산식을 push
            top += 1
            stack[top] = left + right
        elif x== '-':
            top += 1
            stack[top] = left - right
        elif x== '/':
            top += 1
            stack[top] = left // right
        elif x== '*':
            top += 1
            stack[top] = left * right
print(stack[top])

# 후위표기법으로 바꾸기
'''
(6+5*(2-8)/2)
6528-*2/+
'''
stack = [0]*100
top = -1
icp = {'(':3, '*':2, '/': 2, '+': 1, '-': 1}# 계산하기 위해 들어오는 문자의 우선순위
isp = {'(':0, '*':2, '/': 2, '+': 1, '-': 1}# 스택 우선순위

fx = '(6+5*(2-8)/2)'
susik2 = ''
for x in fx:
    if x not in '(+-*/)': # 피연산자
        susik2 += x
    elif x == ')':    # '('까지 pop()
        while stack[top] != '(': # peek
            susik2 += stack[top]
            top -= 1
        top -= 1 # '(' 버림, pop
    else: # '(+-*/'
        if top == -1 or isp[stack[top]] < icp[x]: # 토큰의 우선순위가 더 높으면, 혹은 비어있으면
            top += 1 # push
            stack[top] = x
        elif isp[stack[top]] >= icp[x]:
            while top > -1 and isp[stack[top]] >= icp[x]:
                susik2 += stack[top]
                top -= 1
            top += 1 # push
            stack[top] = x
print(susik2)