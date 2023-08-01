# 결과 => {'A': 3, 'B': 3, 'O': 3, 'AB': 3}
blood_types = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']

# 빈 딕셔너리
new_dict = {}

for blood in blood_types:
    if blood in new_dict:
        new_dict[blood] += 1
    else:
        new_dict[blood] = 1

print(new_dict)

new_dict = {}

for blood in blood_types:
    new_dict[blood] = new_dict.get(blood, 0) + 1
print(new_dict)

new_dict = {}

for blood in blood_types:
    new_dict[blood] = new_dict.setdefault(blood, 0) + 1
print(new_dict)
