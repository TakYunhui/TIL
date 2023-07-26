# Class 정의
# Pascal Case 사용 - 대문자로 시작
# Class - attribute + method
class Person:
    # 속성(변수)
    blood_color = 'red'

    # 메서드
    # __언더바__ : 개발자가 직접 호출하지 않는 메서드(매직 메서드)
    # __init__ : 생성자 메서드, 인스턴스가 호출될 때 자동으로 만들어짐
    # 객체의 초기화 담당
    def __init__(self, name):
        self.name = name

    def singing(self):
        return f'{self.name}가 노래합니다.'

# 인스턴스 생성
singer1 = Person('iu')
singer2 = Person('BTS')

# 메서드 호출
print(singer1.singing())
print(singer2.singing())

# 속성(변수) 사용
print(singer1.blood_color)
print(singer2.blood_color)