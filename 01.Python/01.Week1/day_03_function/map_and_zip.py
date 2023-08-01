def some_func(parm1):
    return parm1 ** 2

print(some_func(3))
print(some_func)


other_var = some_func
print(other_var(3))

numbers = [1, 2]
print(list(map(some_func, numbers)))

# map(function, iterables)
# iterable: 순회 가능한 구조 

def my_map(func, iterable):
    for item in iterable:
        result = func(item)
        print(result, end=' ')

my_map(some_func, numbers)

# 패킹과 언패킹 - map()
# '10 9 120'
# int().input() => ['10', '9', '120']
# int('10')
# int('9')
# int('120')
# <map [10. 9, 12]>
# N, K, M = map(int, input().split())
# N = 10
# K = 9
# M = 120
print('***')
data = list(map(int, input().split()))
N, K, M = map(int, input().split())

print(data)
print(N, K, M)