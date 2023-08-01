from class1 import Pokemon


class Pikachu(Pokemon):
    no = 25
    # 피카츄 클래스 변수 이름이라 내장 함수 예약어 ㄱㅊ
    type = '전기'


    def __init__(self, name, lv=5):
        # super -> 부모 클래스의 메서드를 호출하고자 할 때 사용
        super().__init__()
        # 부모 클래스의 메서드를 직접 호출 -> self 인자로 넘겨야 함
        # Pokemon.__init__(self)
        self.name = name
        self.lv = lv
        # number_of_pokemon은 클래스 변수
        # 상속과는 관련 없이 포켓몬 클래스의 상태 정보 조회
        # -> 그냥 클래스로 가져옴
        # self.number = Pokemon.number_of_pokemon

        
        # 최초의 피카츄가 태어났을 때만, 종 정보를 기록한다.
        # first_child 
        if Pikachu.first_child is None:
            # Pikachu.first_child = self
            super().increase_species('피카츄')


class Metamon(Pokemon):
    no = 132
    type = '노멀'
    def __init__(self, name, lv =5):
        self.skill_1 = name
        # super().__init__()
        self.name = name
        self.lv  = lv

        if Metamon.first_child is None:
            # Metamon.first_child = self
            super().increase_species('메타몽')
            self.skill_1 = '변신'
    def attack(self, target):
        self.type = target.type
        return f'{self.name}이 {target.name}으로 변신했다.'



p1 = Pikachu('지우개')
print(p1.name)
print(p1.skill_1)

p2 = Pikachu('피카츄')
p2.type = '격투'
print(p2.name)
print(p1.type, p2.type)

print(Pokemon.number_of_pokemon)
print(Pokemon.discovered_species)

# 좌측의 패키치가 태어났을 때

p1 = Pikachu('피카츄')
m1 = Metamon('메타몽')
print(Pokemon.discovered_species)
# print(p1.attack(), m1.attack(p1))
print(m1.type)
print(Metamon.type)


# 다중 상속, 여러 클래스를 동시에 상속받을 수 있음
# Pikachu와 Metamon 에서 super() 사용하는 부분 지워둠
# 안 지우면 개판남
# -> mro, Child 가 super() 호출한 주체가 되어버려서...
# class Child(Pikachu, Metamon):

#     def __init__(self, name, lv=5):
#         super().__init__(name, lv)
    
# c1 = Child('피카츄 메타몽')
# print(c1.type)
# print(c1.name)
# print(c1.attack())