# 함수 input -> output
def some_func(parm1):
    # return output
    return parm1 ** 2

num = some_func(3)
print(num)

numbers = [1, 2]
result = numbers.append(3)
print(result)
print(numbers)

result = numbers.pop()
print(result)
print(numbers)


# str 의 특성: immutable
# 문자열은 바뀌지 않는다는 속성을 건드릴 수 없다
# -> 문자열 원본을 바꾸지 않고, 복사본을 반환
char = 'hello'
result = char.replace('e', 'a')
print(result)
print(char)