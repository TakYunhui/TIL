# 0 ~ 9 요소를 가지는 리스트 만들기
# 1. 일반적인 방법
new_list = []
for i in range(10):
    if i % 2 == 1:
       new_list.append(i)
    else:
        new_list.append(str(i))
print(new_list)

# 2. list comprehension
# 일반적인 방법과 마찬가지로 for문 이후 if문
new_list_2 = [i for i in range(10) if i % 2 == 1]
# if-else 가능
# 중첩된 if 가능
# elif 불가능
new_list_3 = [i if i % 2 == 1 else str(i) for i in range(10)]
print(new_list_2)
print(new_list_3)

# 응용
# 새 리스트 만들기 
squared_numbers = [i ** 2 for i in range(10)]
print(squared_numbers)

# 리스트를 생성하는 3가지 방법 비교
# 정수 1, 2, 3을 가지는 새로운 리스트 만들기
# 어떤 게 제일 빨라요??

numbers = ['1', '2', '3']

# 1. for loop
new_numbers = []
for number in numbers:
    new_numbers.append(int(number))
print(new_numbers)

# 2. map
new_number2 = list(map(int, numbers))
print(new_number2)

# 3. list comprehension
new_number3 = [int(number) for number in numbers]
print(new_numbers)
