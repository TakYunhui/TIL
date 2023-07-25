# Q5. 2차원 리스트가 주어질 때, 2중 for문을 활용하면
# 행 → 우선 순회 | 열 ↓ 우선 순회를 자유롭게 진행 할 수 있다.
# 주어진 리스트이 행, 열 우선 순회 결과를 각각 출력하시오.

numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 행 우선 1, 2, 3, 4, 5, 6 , 7, 8, 9
for i in numbers:
    for j in i:
        print(j, end=' ')
    print()



# 열 우선 1, 4, 7, 2, 5, 8, 3, 6, 9
# i = 0, 1, 2 
# j = 0, 1, 2
# j 0, 1, 2로 한 바퀴 도는동안 i = 0 고정 
# numbers[0][0], numbers[1][0], numbers[2][0], ... 
for i in range(len(numbers)):
    for j in range(len(numbers)):
        print(numbers[j][i], end=' ')
    print()

print()

# 가로 N 세로 M 제공
# width = 3
# height = 3
# for i in range(width):
#     for j in range(height):
#         print(numbers[j][i], end=' ')
#     print()


# 대각선 
for i in range(3):
    print(numbers[i][i])
print()


for i in range(3):
    print(numbers[i][3 - (i + 1)])