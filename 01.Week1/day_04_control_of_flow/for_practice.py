# 문자열 순회
country = 'Korea'
for char in country:
    print(char)
'''
K
o
r
e
a
'''
print()

# range 순회
for i in range(5):
    print(i)
'''
0
1
2
3
4
'''
print()

# 인덱스로 리스트 순회
# 리스트의 요소가 아닌 인덱스로 접근하여 해당 요소들을 변경하기
# range 값을 고정하면 다른 input 케이스가 왔을 때 재사용할 수 없기에 
# len을 통해서 index에 접근한다
numbers = [4, 6, 10, -8, 5]
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
print(numbers)
print()

# 중첩된 반복문
# outer - inner 0번째 출력후
# 안 쪽 for문 inner문을 먼저 끝내야
# 위로 올라간다
outers = ['A', 'B']
inners = ['c', 'd']
for outer in outers:
    for inner in inners:
        print(outer, inner)
print()

'''
A c
A d
B c
B d
-> 반복이 총 4회 일어남
-> 반복 횟수: len(outers) * len(inners)
'''

# 중첩 리스트(이차원 리스트) 순회
# 안쪽 리스트 요소에 접근하려면 바깥 리스트를 순회하면서 
# 중첩 반복을 사용해 각 안쪽 반복을 순회
elements = [['A', 'B'], ['c', 'd']]

for elem in elements:
    for item in elem:
        print(item)
'''
A
B
c
d
'''