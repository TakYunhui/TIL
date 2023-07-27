class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print(f'안녕, {self.name}이다.')


class Professor(Person):
    def __init__(self, name, age, department):
        # Person.__init__(self, name, age)
        # 부모 클래스 메서드를 호출하기 위해 사용되는 내장 함수
        super().__init__(name, age)
        self.department = department


class Student(Person):
    def __init__(self, name, age, gpa):
        super().__init__(name, age)
        self.gpa = gpa

p1 = Professor('박교수', 49, '컴공')
s1 = Student('김싸피', 20, 3.5)

p1.talk()
s1.talk()
