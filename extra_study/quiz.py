# reverse() 구현

greeting = 'hi my name istak'

def reverse_prac(data):
    result = ''
    for i in data:
        result =  i + result
    return result

print(reverse_prac(greeting))

# find()

def finding_text(data, finding_str):
    for i in range(len(data)):
        if data[i] == finding_str:
            return i

print(finding_text(greeting, 'h'))

def word(data, finding_str):
    words = data.split()
    indices = 0
    for i, word in enumerate(words):
        print(i, word)
        if word == finding_str:
            indices = i
    return indices

print(word(greeting, 'tak'))


# len 구현
statement = 'hi my name is tak'
anything = [1, 2, 3, 4, 5, 6, 7, 8, 89]

def length_sol(data):
    count = 0
    for i in data:
        count += 1
    return count

print(length_sol(statement))
print(length_sol(anything))


# max, min
# 부등호만 바꿈
data = [10, 20 , 30 ,40, 50, 100]

def max_sol(data):
    result = data[0]
    for num in data:
        if num > result:
            result = num
    return result

print(max_sol(data))
        

