# oop : 객체지향
# 파이썬 클래스
# OOP(객체 지향 프로그래밍), Self, 인스턴스 메소드, 인스턴스 변수

# 클래스 and 인스턴스 차이 이해
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 접근 가능, 공유
# 인스턴스 변수 : 객체마다 별도 존재



#객체(Object)란 자신 고유의 속성을 가지는 물리적, 추상적인 모든 대상을 일컫는다.
#클래스(Class)란 객체들을 소프트웨어 내에서 구현하기 위해 만든 설계도이다.
#이를 통해 생성된 객체 하나하나를 인스턴스(Instance)라고 부른다.
#대체로 객체와 인스턴스는 혼용해서 표현한다.

# 예제1
class Dog: # object 상속
    # 클래스 속성
    species = 'firstdog'   # 공요의 클래스 변수
    
    # 초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name  # 나만의 인스턴스 변수
        self.age = age
        
# 클래스 정보
print(Dog)

# 인스턴스화
a = Dog("mikky", 2)
b = Dog("baby", 3)

# 비교
print(a == b, id(a), id(b))

# 네임스페이스
print('dog1', a.__dict__)
print('dog2', b.__dict__) 

# 인스턴스 속성 확인
print('{} is {} and {} is {}'.format(a.name, a.age, b.name, b.age))

if a.species == 'firstdog':
    print('{0} is a {1}'.format(a.name, a.species))

print(Dog.species)  # 클래스로도 바로 접근 가능
print(a.species)    # 인스턴스화 된 변수로도 접근 가능
print(b.species) 

# 예제2
# self의 이해
class SelfTest:  
    def func1():  # 클래스 메소드
        print('Func1 called')
    def func2(self):   # 인스턴스 매소드
        print(id(self))
        print('Func2 called')


f = SelfTest()

# print(dir(f))
print(id(f))

# f.func1() # 예외 self가 없음
f.func2()

# SelfTest.func2() # 예외 self가 있음 
SelfTest.func1()
SelfTest.func2(f)

# 예제3
# 클래스 변수, 인스턴스 변수
class Warehouse:
    # 클래스 변수 
    stock_num = 0 # 재고
    
    def __init__(self, name):
        # 인스턴스 변수
        self.name = name
        Warehouse.stock_num += 1
    
    def __del__(self):   # 객체가 소멸할때 자동 호출
        Warehouse.stock_num -= 1

user1 = Warehouse('Lee')
user2 = Warehouse('Cho')

print(Warehouse.stock_num)

# Warehouse.stock_num = 0.0094
print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print('before', Warehouse.__dict__)
print('>>>', user1.stock_num)

del user1
print('after', Warehouse.__dict__)

# 예제4
class Dog: # object 상속
    # 클래스 속성
    species = 'firstdog'
    
    # 초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def info(self):
        return '{} is {} years old'.format(self.name, self.age)
        
    def speak(self, sound):
        return "{} says {}!".format(self.name, sound)
    

# 인스턴스 생성
c = Dog('july', 4)
d = Dog('Marry', 10)
# 메소드 호출
print(c.info())
print(d.info())
# 메소드 호출
print(c.speak('Wal Wal'))
print(d.speak('Mung Mung'))