# 함수 구조에 return을 안 쓰는 경우
   
# func_name(parm1, parm2):
#     return parm1 + parm2

# func_name(1, 2) # 함수를 호출한 것
# 함수를 호출하는 행위 -> 평가 후 값을 내는 표현식
# print(func_name(1, 2))

def func_name2(parm1, parm2):
    print(parm1 + parm2)

func_name2(1, 2) 
print(func_name2(1, 2))

# 3 - 호출된 func_name2 안 코드 실행해 출력
# 3 - print(func_name2(1, 2))의 값
# None - 위의 함수를 들어가니 parm1, parm2 값이 안 주어져서 아무 것도 없는 값



# 키워드 인자 
def greeting(name, age):
    print(f'안녕하세요, {name}님! {age}살이시군여.')
# 모든 매개 변수에 키워드 인자 형식으로 값을 넘겼을 때.
# 실행 뒤 return None
# 하지만 return으로 종료되고, 별다른 print 명령이 없으므로 None은 출력되지 않는다.
greeting(age= 30, name='홍길동')

print('첫', '두', '세', end='\t', sep=':')
print('다음 줄')


# 가변인자로 매개변수를 정의하면
# 함수를 호출할 때, N개의 값을 넘겨도 모두 하나의 변수에 할당
# 이때, tuple 형태로 할당 된다.
def func(*args, sep=' '):
    print(args, sep)
func('첫', '두', '세')