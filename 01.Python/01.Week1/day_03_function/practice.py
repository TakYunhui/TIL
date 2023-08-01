# print 함수에 여러 개의 인자 넣기 가능
print('hi', 'aaa', 'bbb')

# 임의의 인자 목록
# 매개변수 앞에 * 붙이기
# 여러 개의 인자를 tuple로 처리
def calculate_sum(*args):
    print(args) # (1, 2, 3, 4, 5)

calculate_sum(1, 2, 3, 4, 5)

# 임의의 키워드 인자 목록
# 매개변수 앞에 ** 붙이기
# 여러 개의 인자를 dictionary로 처리
def calculate_sum2(**kwargs):
    print(kwargs) 

calculate_sum2(name='Alice', age=30, address='korea')

# 범위
def my_func():
    # local scope에 정의된 num
    num = 1
# 함수 바깥에서 num이라 하면 scope가 다르기에 NameErroe발생
# print(num) 

# 재귀 함수 예시 - 팩토리얼
def factorial(n):
    # 종료 조건: n이 0이면 1을 반환
    if n == 0:
        return 1
    # 재귀 호출: n과 n-1의 팩토리얼을 곱한 결과 반환
    return n * factorial(n-1)

result = factorial(5)
print(result)

# map 함수
numbers = [1, 2, 3]
result = map(str, numbers)
print(result)
print(list(result)) # ['1', '2', '3']

# map을 안 쓰면, ...
result = []
for number in numbers:
    result.append(str(number))
print(result)

# zip 함수 
names = ['Alice', 'Bob', 'Charlie']
ages = [30, 25, 35]

for name, age in zip(names, ages):
    print(f'{name} is {age} years old.')