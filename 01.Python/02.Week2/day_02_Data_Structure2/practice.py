# 혈액형 인원수 세기
# 결과 => {'A': 3, 'B': 3, 'O': 3, 'AB': 3}
blood_types = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']

# []
new_dict = {}
# 1. blood_types을 순회하면서
for blood_type in blood_types:
    # 기존에 키가 이미 존재한다면,
    # count 증가
    # 키가 존재하지 않는다면 (처음 설정되는 ㅣ)
    # count 1로 설정
    if blood_type in new_dict:
        # 기존 키의 값을 + 1
        new_dict[blood_type] += 1
    else:
        new_dict[blood_type] = 1
print(new_dict)




# .get()
new_dict = {}
for blood_type in blood_types:
    # .get의 default 값을 0으로 준다
    # 1이 아닌 이유?
    # 기존에 있는 값이라면 1을 더해주기 때문에 최종 결과값이 1 더 증가하기 때문
    new_dict[blood_type] = new_dict.get(blood_type, 0) + 1

print(new_dict)

# .setdefault()
new_dict = {}
for blood_type in blood_types:
    new_dict.setdefault(blood_type, 0)
    new_dict[blood_type] += 1
print(new_dict) 

# .get : 키가 없으면 None 또는 default 값 반환()
# .setdefault: 조회된 키가 없으면 default 연결 값을 새로 딕셔너리에 추가