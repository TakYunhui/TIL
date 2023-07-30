numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 행 순회 
for i in range(len(numbers)):
    for j in range(len(numbers)):
        print(numbers[i][j], end=' ')
    print()

# 열순회
for i in range(len(numbers)):
    for j in range(len(numbers)):
        print(numbers[j][i], end=' ')
    print()

# 대각선
for i in range(len(numbers)):
    print(numbers[i][i])

# 대각선 반대
for i in range(len(numbers)):
    print(numbers[i][3 - (i + 1)])