# 리스트 순회에 인덱스 접근을 하는 이유
# 1. 리스트 값의 원하는 범위만 가져오기
# 2. 리스트 안 요소들 변경 가능

dusts = [50, 60, 70, 80]

# 1번 예시
for index in range(1, len(dusts), 4):
    print(dusts[index])
    
# 2번 예시
for index in range(len(dusts)):
    dusts[index] = 0
print(dusts)

# 중첩 리스트 순회
numbers = [
   # 0  1  2
    [1, 2, 3], # 0
   # 0  1  2
    [4, 5, 6], # 1
   # 0  1  2
    [7, 8, 9]  # 2
]

for number in numbers: # number | [1, 2, 3] | [4, 5, 6] | [7, 8, 9]
    for num in number:
        print(num)
    print('=' * 30)


for numbers_index in range(len(numbers)): # number | [1, 2, 3] | [4, 5, 6] | [7, 8, 9]
    scores = numbers[numbers_index]
    print(scores)
    for scores_index in range(len(scores)):
        print(numbers_index, scores_index)