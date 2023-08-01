# break
# 프로그램 종료 조건 만들기
number = int(input('양의 정수를 입력해주세요.: '))
while number <= 0:
    if number == -9999:
        print('프로그램을 종료합니다.')
        break
    if number < 0:
        print('음수를 입력했습니다.')
    else:
        print('0은 양의 정수가 아닙니다.')
    
    number = int(input('양의 정수를 입력해주세요.: '))

print()

# 리스트에서 짝수 찾기
numbers = [1, 3, 5, 6, 7, 8, 11]
found_even = False
for num in numbers:
    if num % 2 == 0:
        print('첫 번째 짝수 찾음!:', num)
        found_even = True
        break

if not found_even:
    print('짝수를 찾지 못했습니다.')


# continue
# 다음 반복(코드 XX)으로 넘어가기
for num in numbers:
    if num % 2 == 0:
        continue
    print(num)