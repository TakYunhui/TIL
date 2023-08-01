numbers = [1, 2, 3]

# 1. 할당
list1 = numbers

# 2. 슬라이싱
# 복사본 생성 
# 다른 주소를 바라봄
list2 = numbers[:]

numbers[0] = 100

print(list1) # [100, 2, 3]
print(list2) # [1, 2, 3]