# Chapter05-0
# 함수란? 완전 함수 기초 설명
# 파이썬 함수 쌩기초

# 종류
# 1.매개변수가 필요한 함수
# 2.매개변수가 필요하지 않은 함수
# 3.결과값을 반환하는 함수(return)
# 4.결과값을 반환하지 않는 함수



# 함수 종류
# def function_name(parameter):
#     code

# 예제1 : 매개변수 필요X
def function1():
    print('예제1 호출')


# 예제2 : 매개변수 필요O
def function2(a, b):
    print('예제2 호출', a, b)


# 예제3 : 결과값 반환X
def function3(x, y):
    print('예제3 호출', x, y)


# 예제4 : 결과값O, 반환O
def function4(x, y):
    return x + y


# 실행
function1()
function2(10, 20)   #입력값이 필요함
function3(30, 40)

function4(50, 50)
r = function4(50, 50)

print('예제4 호출', r)