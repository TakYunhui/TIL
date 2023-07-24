# Data Structure
# print(help(list))

# 문자열.title()
my_str = 'veni is cute'
print(f'첫 번째 출력:{my_str}')

print(f'두 번째 출력:{my_str.title()}')
print(f'세 번째 출력:{my_str}')

# 문자열.strip 
# 시작과 끝에 있는 공백 제거(기본)
# [chars]: 지정 문자 가능 
hi =  '  Hello,  World   '
print(hi.strip(' ')) # Hello, World
# -> 가운데 공백도 없애는 방법은 없나?

text = 'heLLo, WorLd!'
new_text = text.swapcase().replace('l', 'z')
print(new_text)


print('-----이 다음은 리스트 -------')
# 리스트 추가
numbers = [1, 2, 3]
numbers2 = [4, 5, 6]
# print(numbers.append(numbers2)) -> None
# print(numbers.extend(numbers2)) -> None
# Why? 복사본 반환 x, 원본을 바꾼 것!
numbers.append(numbers2)
print(numbers)

numbers.extend(numbers2)
print(numbers)

# 리스트 정렬 
# sort 메서드
new_numbers = [3, 2, 1]
print(new_numbers.sort())
# -> 원본을 바꾸기에 반환 x 
# None

# sorted 함수
new_numbers2 = [3, 2, 1]
print(sorted(new_numbers2)) 
# -> 원본을 건드리지 않고 복사본을 만들어 반환