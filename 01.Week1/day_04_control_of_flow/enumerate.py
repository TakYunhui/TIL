# enumerate
fruits = ['사과', '귤', '오렌지']

for index, fruit in enumerate(fruits):
    print(f'인덱스 {index}: {fruit}')

result = ['a', 'b', 'c']
print(enumerate(result)) # <enumerate object at 0x0000027E2C0B71C0>
print(list(enumerate(result))) # [(0, 'a'), (1, 'b'), (2, 'c')]
for index, elem in enumerate(result):
    print(index, elem)