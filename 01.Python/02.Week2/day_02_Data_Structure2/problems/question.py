info = {'name': '홍길동', 'age': 3}
result = info.get('name')
print(result)

result2 = info['name']
print(result2)

# 1. get() = 메서드임 | 함수임
# 2. 함수 반환할 값이 없으면 None 반환함
result3 = info.get('address')
print(result3)

# 존재하지 않는 키를 찾아서 KeyError
# result4 = info['address']
# print(result4)

info['address'] = '서울'
print(info)

result5 = info.get('address', '없음')
print(result5)
print(info)