# Q4. 혈액형 타입을 담은 blood_types리스트가 주어 질 때,
# 각 혈액형 타입을 키로, 누적 수를 value로 하는 딕셔너리 blood를 만들어 반환하는
# 함수 make_blood를 작성하시오


blood_types = ['A', 'B', 'O', 'AB', 'A', 'O', 'B', 'AB', 'A', 'B']

# make_blood(blood_types) -> {'A': 3, 'B': 3, 'AB': 2, 'O': 2}

def make_blood(blood_types):
    blood = {}
    for blood_type in blood_types:
        blood[blood_type] = blood.get(blood_type, 0) + 1
    print(blood)

make_blood(blood_types)