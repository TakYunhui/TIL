# Q1. 1부터 인자로 넘겨받은 숫자까지의 합을 구하는
# 함수 make_sum을 작성하시오.

# make_sum(10) -> 55

def make_sum(num):
    result = 0
    for i in range(num+1):
        result += i
    return result


print(make_sum(10))

