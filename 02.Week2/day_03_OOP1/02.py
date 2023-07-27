# Person 정의
class Person:
    name = 'unknown'

    # 인스턴스 메서드
    # 사용하는 주체가 인스턴스이기에
    def talk(self):
        print(self.name)

p1 = Person()
p1.talk() # unknown
# p2 인스턴스 변수 설정 전/후

p1.address = 'korea'
print(p1.address)

# p2 = Person()
# p2.talk() # unknown

# p2.name = 'Kim'
# p2.talk() # Kim

# print(Person.name) # unknown
# print(p1.name) # unknown
# print(p2.name) # Kim

