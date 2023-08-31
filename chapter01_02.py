#chapter 02-2

#기본 선언
n = 700

#출력
print(n)
print(type(n))
print()

#동시 선언
x = y = z = 700
print(x, y, z)
print()

#선언
var = 75

#재선언
var = "change value"

#출력
print(var)
print(type(var))

# object references
# 변수 값 할당 상태
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 셍성
# 3. 콘솔 출력

#예1
print(300)
print(int(300))

#예2
n = 777

print(n, type(n))
print()

m = n
print(m, n)
print(type(m), type(n))
print()

m = 400
print(m, n)
print(type(m), type(n))
print()

#객체의 고윳값 확인
m = 800
n = 655

print(id(m))
print(id(n))
print(id(m) == id(n))  # 다름
print()

# 같은 오브젝트 참조
m = 800
n = 800

print(id(m))
print(id(n))
print(id(m) == id(n))  # 같음 # 같은 값이면 하나의 오브젝트로 참조
print()

# 다양한 변수 선언
# camel case : 처음은 소문자 다른 것은 대문자 - method
# pascal case : 처음도 대문자 - class
# snake case : nnumber_of_college : _로 이어줌 - 변수

# 허용하는 변수 선언 법
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE = 7
AGE = 7

# 예약어는 변수명으로 불가능

