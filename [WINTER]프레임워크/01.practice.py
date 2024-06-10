# 23.11.27
# 클래스(템플릿) 만들기
print('클래스 만들기')
class Person:
    def __init__(self):
        a = 0
        b = 0

    def abc(self):
        print('hi')

# 인스턴스(객체) 만들기
t = Person() # 생성자 호출 - 스택택t.abc()
t.abc()

print('---------------')

class Zergling:
    def __init__(self):
        self.hp = 80
        self.mana = 200

    def attack(self):
        self.hp += 1
        self.mana -= 10

    def move(self):
        self.hp -= 10
        self.mana += 5

    def status(self):
        print(self.hp, self.mana)


z = Zergling()
z.status()
z.move()
z.status()
z.attack()
z.status()

print('---------------')

# 서버 코드 - 클래스
class Calculator:
    def __init__(self):
        self.result = 0

    def plus(self, int, int2):
        self.result = int + int2

    def minus(self, int, int2):
        self.result = int - int2

    def divide(self, int, int2):
        self.result = int // int2

    def multiple(self, int, int2):
        self.result = int * int2

    def printResult(self):
        print(self.result)


c = Calculator()
c.plus(1, 2)
c.printResult()
c.minus(1, 2)
c.printResult()
c.divide(4, 2)
c.printResult()
c.multiple(4, 2)
c.printResult()

print('---------------')

class GameMachine:
    def __init__(self):
        self.totalCoin = 0

    def inputCoin(self, int):
        self.totalCoin += int
        if self.totalCoin > 10:
            self.totalCoin -= int

    def playGame(self):
        self.totalCoin -= 1

    def printCoin(self):
        print(self.totalCoin)

game = GameMachine()
game.inputCoin(2)
game.printCoin()
game.inputCoin(9)
game.printCoin()

print('---------------')
print('상속')
class SpeedRobot:
    # Super class
    # 상속될 요소는 __init__에 적지 않는다
    hp = 100

    def move(self):
        self.hp -= 1

    def stop(self):
        self.hp += 5

    def run(self):
        self.hp -= 10

    def walk(self):
        self.hp -= 5


class PowerRobot(SpeedRobot):
    def __init__(self):
        self.mana = 50

    def attack(self):
        self.mana -= 10

    def jump(self):
        self.mana -= 30

    def status(self):
        print(self.hp, self.mana)


robot = PowerRobot()
robot.run()
robot.status()

print('---------------')
print('오버라이딩')
class Phone:
    def call(self):
        print('Calling...')

class SmartPhone(Phone):
    def call(self):
        print('SmartCalling...')

phone = SmartPhone()
phone.call()