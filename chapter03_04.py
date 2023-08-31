# chapter03_04
# 파이썬 튜플
# 튜플 자료형(순서o, 중복o, 수정X, 삭제X) ---> 불변

# 선언
a = ()
b = (1,) # 원소가 하나일때는 ,를 찍어야 튜플이 됨
c = (11, 12, 13, 14)
d = (100, 1000,'Ace', 'Base', 'Captine')
e = (100, 1000, ('Ace', 'Base', 'Captine'))

# 인덱싱
print(">>>>>>>")
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('e - ', e[-1][1])
print('e - ', list(e[-1][1]))  # 리스트로도 튜플을 형 변환이 가능하다

# 튜플은 수정이 안됨

# 슬라이싱
print('>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[2][1:3])

# 튜플 연산
print('>>>>>')
print('c + d - ', c + d)
print('c * 3 - ', c * 3)
# print("c[0] + 'hi' - ",c[0] + 'hi')
print("'Test' + c[0] - ", 'Test' + str(c[0]))

# 튜플 함수
a = (5, 2, 3, 1, 4)

print('a - ', a)
print('a - ', a.index(5))  # 5가 어디 인덱스에 있나
print('a - ', a.count(4))

# 팩킹 & 언팩킹(Packing, and Unpacking)

# 팩킹 ----> 묶는 것
t = ('foo', 'bar', 'baz', 'qux')

# 출력 확인
print(t)
print(t[0])
print(t[-1])

# 언팩킹1
(x1, x2, x3, x4) = t

print(type(x1), type(x2), type(x3), type(x4))  # str임
# 출력확인
print(x1)
print(x2)
print(x3)
print(x4)

# 언팩킹2
(x1, x2, x3, x4) = ('foo', 'bar', 'baz', 'qux')

# 출력 확인
print(x1)
print(x2)
print(x3)
print(x4)

# 팩킹 & 언팩킹
t2  =1, 2, 3  # 괄호가 없어도 튜플
t3 = 4, 
x1, x2, x3 = t2
x4, x5, x6 = 4, 5, 6

# 출력 확인
print(t2)
print(t3)
print(x1,x2,x3)
print(x4,x5,x6)