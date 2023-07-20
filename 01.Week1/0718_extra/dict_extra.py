dictionary ={'키': '밸류'}
# 1. 파이썬에서 문자열은 '' ""로 묶어서 표기
# 2. f-string | 문자열 보간법
# 3. f-string이란 파이썬의 문자열에 포함된 기능
# 4. '{dictionary[' 키 ']}'
# (X) print(f'{dictionary['키']}') -> ''가 겹쳐서 x
print(f'{dictionary["키"]}')

print(f'함수: {sum([1, 2])}')

# slicing
#            N    M-1
# sequence[start: end : step] step만큼 건너 뛰어간다.
# step == default = 1

my_range = range(1, 10, 2)
print(list(my_range))

# 순서(위->아래)대로 실행
# 딕셔너리: 순서와 중복이 없는 변경 가능한 자료형
# 키는 그대로, 뒤의 값을 가지게 됨 
dictionary = {'apple': '사과', 'apple': '스티븐 잡스'}
print(dictionary)

# 파이썬 업데이트로 순서가 있는 것처럼 보이는 것 뿐
# 순서 보장 xxxx
for key, value in dictionary.items():
    print(key, value)

