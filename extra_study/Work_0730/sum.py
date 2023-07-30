# make_sum(10) -> 55
def make_sum(number):
    result = 0
    for num in range(number + 1):
        result += num
    return result


print(make_sum(10))