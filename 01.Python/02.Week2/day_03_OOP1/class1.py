# 함수는 def 뒤에 함수 이름
# 클래스는 class 뒤에 클래스 이름
# 단, 클래스 name의 컨벤션은 앞글자 대문자 (PascalCase를 사용)
# 컨벤션은 상호 간의 약속이다. 어디서 어떤 라이브러리를 사용하든, PascalCase로 작성된 
# 값들은 모두 클래스라는 사실을 별도로 내부 코드를 확인하지 않아도 알 수 있다.UnboundLocalError
# 의문? list, str, int 얘네는 PascalCase 아닌데? -> 이건 예외. 파이썬 내부적으로 이미 만들어져있으므로...

# library 클래스에서는
    # 책의 관리 | 책의 정보 : 제목, 작성자, 보유 권수 인스턴스 생성
    # 총 보유 책 권수
    # 대여 시스템 메서드


class Library:
    '''
    책 각각의 정보를 관리하는 class 입니다.
    Library class를 통해서는 book instance를 생성할 수 있습니다.
    또한, 책 대여 시스템을 활용할 수 있습니다.
    '''

    # 클래스 변수
    # 책이 생성 될 때 마다 1씩 증가
    number_of_book = 0

    # 생성자: 클래스에 의해 인스턴스가 생성되는 순간, 실행되는 매직 메서드
    # double underscore로 작성되는 메서드들은 모두 매직 메서드
    # 파이썬이 내부적으로 특정한 동작을 하도록 만들어놓은 메서드들

    # self의 역할 : 호출 대상 인스턴스 자체를 의미 
    # numbers.append(3) -> append
    # self는 함수 정의 할 때, 적는 매개변수
    # -> 변수 작성시 규칙을 따라간다!
    def __init__(self, title, author, volumes=1):
        self.title = title
        self.author = author
        # 책 정보에 책 마다의 보유 권수를 따로 저장
        # 일반적으로, 동일한 책은 1권씩 추가
        # 특별한 경우에만, 여러권이 추가된다면?
        # 기본 인자를 이용한다!
        self.volumes = volumes
        # 클래스 변수 호출 하여 값 증가
        # 아래 방식은 생성자에서만 허용하는 느낌
        # 되도록 클래스 메서드를 호출하는 것을 권장
        # Library.number_of_book += 1
        Library.increase_book(volumes)
    
    # 함수 위에 @ 형식으로 데코레이터를 정의하게 되면,,,,
    # 그 데코레이터는 (자기에게 맡겨진 기능을 수행) -> 함수
    # @classmethod 데코레이터 아래에 정의된 메서드는
    # 첫 번째 인자로, 호출한 대상의 소속 clss를 첫번째 인자로 넘기도록 바꿈
    '''
    def classmethod(func):
        def wrapper():
            func(self.class)
    
    '''

    # 해당 함수는 첫번째 인자를 호출 주체의 class를 받게 된다
    # 인스턴스가 호출시에도 첫번째 인자는 호출한 인스턴스의 
      # 클래스를 인자로 넘겨주기에
      # 인스턴스는 클래스 메서드도 호출 시 
      # 정상 작동하지만, 그렇게 쓰지는 말자!!
    @classmethod
    def increase_book(cls, volumes):
        cls.number_of_book += volumes
    
    # 출력에 이용
    def __str__(self):
        return self.title

    # 소멸자
    # 파이썬 실행이 끝나면 소멸됨
    # def __del__(self):
    #     print(f'{self.title}책을 제거하였습니다!')
    #     return None

        # rental_system 메서드
        # 1. 인자는 유저와 책 인스턴스를 받는다.
        # 2. 대여하고자 하는 책 수도 함께 받는다.

    # rental_system은 무슨 메서드로 만드는게 적합할까?
    # -> class method
    @classmethod
    def rental_system(cls, user, book, volumes=1):
        # 3. 대여하고자 하는 책 수만큼 라이브러리의 총 책 수 감소
        cls.number_of_book -= volumes
        # 4. 대여되는 책의 보유 수량 감소
        # book.volumes -= volumes
        book_volumes = book.decrease_volumes(volumes)

        if book_volumes:
            # 5. 유저 이름과 책 이름, 대여 권수 출력
            print(f'{user.name}님이 {book.title}책을 {volumes}권 만큼 대여하였습니다.')
            print(f'{book.title}은 {book.volumes}권 만큼 남았습니다.')
        else:
            print(f'{book.title}이 {volumes}권 만큼 보유하고 있지 않아 대여할 수 없습니다.')
    
    def decrease_volumes(self, volumes):
        if self.volumes - volumes < 0:
            return False
        else:
            self.volumes -= volumes
            return True
        
    @staticmethod
    def information():
        print(
    '''
    도서 관리 서비스입니다.
    책을 등록할 수 있습니다.
    등록되어있는 유저와 책 정보로 책을 대여할 수 있습니다.
    '''
        )

Library.information()


# Library 클래스에 의해 생성되는 book1 인스턴스는
# 자신만의 고유한 title과 author 정보를 가질 수 있다.
# numbers = list(1)
# numbers = list([1, 2])
book1 = Library('홍길동전', '허균')
print(book1)
print(type(book1))
# print(book1.title, book1.author)
# print(book1.volumes)


book2 = Library('레미제라블', '빅토르 위고', 10)
print(book2)
# print(book2.title, book2.author)    
# print(book2.volumes)
print('=' * 30)
print(Library.number_of_book, 'Library')
print(book1.number_of_book, 'book1')
print(book2.number_of_book, 'book2')
    

# User 클래스에서는
    # 유저 정보 관리 | 유저 정보 : 이름, 나이 
class User:
    # 클래스 변수
    number_of_people = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        User.increase_user()

    @classmethod
    def increase_user(cls):
        cls.number_of_people += 1
    
    def __str__(self):
        return self.name
    


# N = 등록해야할 유저의 수
N = 4
name = ['김시습', '허균', '남영로', '빅토르위거']
age = [10, 20, 30, 40]

person1 = User('김준호', 12)

user_list = []
for index in range(N): # 0 1 2 3
    # person = User('김시습', 10) | index : 0
    # person = User('허균', 20)   | index : 1
    person = User(name[index], age[index])
    user_list.append(person)
print(user_list)

Library.rental_system(person1, book1)
Library.rental_system(person1, book1)