# 진법 변경
print(bin(12))
print(oct(12))
print(hex(12))

# 실수 근삿값 출력
print(2 / 3)
print(5 / 3)

# 실수 연산 시 해결책
a = 3.2 - 3.1
b = 1.2 - 1.1

# 1. 임의의 작은 수 활용
print(abs(a - b) <= 1e-10)

# 2. math 모듈 활용
import math
print(math.isclose(a, b))

# 지수(제곱하는 횟수) 표현 방식
# 314 * 0.01
number = 314e-2

# float 
print(type(number))

# 3.14
print(number)

# Escape sequence 예시
print('철수야 \'안녕\'')

'''
이 다음은 엔터입니다
'''
print('이 다음은 \n 엔터입니다.')

# f-string
bugs = 'roaches'
counts = 13
area = 'living room'
print(f'Debugging {bugs} {counts} {area}')

# f-string 응용: f-string advanced
greeting = 'hi'
# 10칸 오른쪽 두기
print(f'{greeting:>10}')
# 10칸 가운데 두기 
print(f'{greeting:^10}')
# 소수점 자리 수 표기
print(f'{3.141592:.4f}')


# 인덱싱과 슬라이싱 with str
my_str = 'hello'
print(my_str[0])
print(my_str[2:4])
print(my_str[0:5:2])
# 음수 인덱스를 이용해 문자열 뒤집기
print(my_str[::-1])

# 리스트 
my_list_1 = []
my_list_2 = [1, 'a', 3, 'b', 5]
my_list_3 = [1, 2, 'a', 'b', [my_str, my_list_2]]

print(my_list_3[4][0])

# 튜플
my_tuple_1 = ()
my_tuple_2 = (1,)

x, y = 10, 20
x = 30

print(x)

# 딕셔너리
my_dict1 = {}
my_dict2 = {'key': 'value'}
print(my_dict2['key'])

# 세트
my_set_1 = set()
my_set_2 = {1, 2, 3}
my_set_3 = {1, 1, 1} # 1 중복 제거

# 합집합
print(my_set_1 | my_set_2) 
# 차집합 
print(my_set_2 - my_set_3) 
# 교집합
print(my_set_1 & my_set_2)

# None
variable = None
print(variable)

# 불변과 가변
# my_str[0] = 'z'
# TypeError: 'str' object does not support item assignment