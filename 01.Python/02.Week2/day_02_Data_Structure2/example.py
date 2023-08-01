# set method
# .remove & .discard
# .remove(x): 존재하지 않는 값 삭제를 시도하면 KeyError
# .discard(x): remove와 달리 에러 X 
my_set = {1, 2, 3}
my_set.discard(10)
print(my_set.discard(10)) # None

# my_set.remove(10)

element = my_set.pop()
print(element)
print(my_set)

# 딕셔너리 접근
my_dict = {
    'name' : 'Yunhui',
    'home' : 'Busan'
}

print(my_dict['name'])
print(my_dict.get('name'))

# 찾고자하는 키가 없을 때
# print(my_dict['age']) # KeyError
print(my_dict.get('age')) # None
print(my_dict.get('age', 'Unknown')) # Unknown

person = {'name': 'Sojung', 'age': 29}

print(person.keys())
for key in person.keys():
    print(key)

print(person.values())
for value in person.values():
    print(value)

print(person.items())
for key, value in person.items():
    print(key, value)

# print(person.pop('age'))
print(person.pop('country', 'country 키는 없어요.'))

# 키와 연결된 값 반환 
# 키가 없다면 default를 추가
print(person.setdefault('country', 'Korea'))
# 이미 있는 키면 기존의 연결된 값 반환
print(person.setdefault('age', 50))
print(person)


# 얕은 복사의 한계
# 복사가 되다 만 녀석
a = [1, 2, [1, 2]]
b = a[:]
b[2][0] = 999
print(a, b)

c = a.copy()
c[2][0] = 1004
print(a, c)

# 깊은 복사
import copy
original_list = [1, 2, [1, 2]]

deep_copied_list = copy.deepcopy(original_list)
deep_copied_list[2][0] = 999

print(original_list, deep_copied_list) # [1, 2, [1, 2]] [1, 2, [999, 2]] 
