class Person:
    gene = 'XYZ'
    def __init__(self, name):
        self.name = name

    def greeting(self):
       return f'안녕, {self.name}이다.'


class Mom(Person):
    gene = 'XX'

    # 생성자 메서드 적어주는 게 정석
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def swim(self):
        return '엄마가 수영'


class Dad(Person):
    gene = 'XY'

    def __init__(self, name):
        super().__init__(name)

    def walk(self):
        return '아빠가 걸어'
    
 
# class FirstChild(Dad, Mom, Dad): TypeError: duplicate base class Dad
class FirstChild(Dad, Mom):
    mom_gene = Mom.gene
    person_gene = Person.gene

    def __init__(self, name, age):
        Mom.__init__(self, name, age)

    def swim(self):
        return '첫째가 수영'

    def cry(self):
        return '첫째가 응애'

baby1 = FirstChild('아가', 1)
print(baby1.cry()) 
print(baby1.swim())
print(baby1.walk())

# 상속 순서대로 가져옴 
print(baby1.gene) # XY 
print(baby1.mom_gene)
print(baby1.person_gene)

print(FirstChild.mro())