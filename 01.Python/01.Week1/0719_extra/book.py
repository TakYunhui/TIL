number_of_book = 100

# def 함수이름(매개변수):
def decrease_book(number): # 한 번에 대여하는 책의 수
    # decrease_book 함수를 기준으로, 들여쓰기 안쪽 코드 block 영역을
    # local scope로 지칭한다.
    # print(number, '넘겨 받은 인자 출력 해보기')
    # double = number * 2
    # print(double, '넘겨 받은 인자 2배로 만들기')
    
    # 함수의 최종 역할
    # return이 없으면 None을 파이썬이 알아서 반환
    # LEGB 탐색 룰에 따라 global에 선언한 number_of_book 변수의 값을 찾아서 계산.
    global number_of_book
    number_of_book -= number
    
    print(number_of_book, '대여한 수 만큼 감소한 책의 수')

num = 3
# 함수 이름(전달 인자)
# 전달 인자와 매개변수의 변수 명이 반드시 같아야 할 이유가 없다.
# expression -> eval -> val -> return 
# 함수 내부에 return 되는 값이 없으면 기본 규칙을 위반한다.
# 따라서, 파이썬은 자동으로 함수가 return 해주는 값이 없으면 -> 값이 없음을 나타내는 None을 return 해준다.
result = decrease_book(num) # 함수를 호출한다  | None 
print(number_of_book)