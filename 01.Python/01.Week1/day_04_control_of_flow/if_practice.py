# 조건문 
a = 5 
if a > 3:
    print('3 초과')
else:
    print('3 이하')

# 복수 조건문
dust = 350
if dust > 150:
    print('매우 나쁨')
    if dust > 300:
        print('위험해요! 나가지 마세요!')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    print('좋음')

# 홀수 짝수 비교 조건문
num = int(input('숫자를 입력하세요 : '))

# if statement
# num이 홀수라면(2로 나눈 나머지가 1이라면)
# if num % 2: -> 자동 형 변환으로 True로 받음
# 명시적인 코드 작성 권장
if num % 2 == 1:
    print('홀수입니다.')
# num이 홀수가 아니라면(짝수면)
else:
    print('짝수입니다.')

