# chapter03-01
# 숫자형

# 파이썬 지원 자료형
"""
int : 정수
float : 실수 
complex : 복소수
bool : 불린
str : 문자열(시퀀스)
list : 리스트(시퀀스)
tuple : 튜플(시퀀스)
set : 집합
dict : 사전

"""

# 데이터 타입
str1 = "python"
bool = True
str2 = "anaconda"
float = 10.0 # 10 == 10.0
int  = 7
list = [str1, str2]
dict = {
    "name": "Machine Learning",
    "version": 2.0
}
tuple = (7, 8, 9)
set = {3, 5, 7}

# 데이터 타입 출력
print(type(str1))
print(type(bool))
print(type(str2))
print(type(float))
print(type(int))
print(type(dict))
print(type(tuple))
print(type(set))

# 숫자형 연산자
"""

/
// : 몫
% : 나머지
abs(x) : 절댓값
pow(x, y) x ** y -> 2 ** 3

"""
x, y = divmod(100, 8)  # x에는 몫 y에는 나머지
print(x, y)


#외부 모듈
import math

print(math.ceil(5.1)) # x이상의 수 중에서 가장 작은 정수
print(math.pi)