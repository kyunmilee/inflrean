# chapter03-03
# 파이썬 리스트
# 리스트 자료형( 순서, 중복, 수정, 삭제 모두 가능)

# 선언
a = []
print(type(a))
b = list()
c = [70, 75, 80, 85]
print(len(c))
d = [1000, 10000, 'Ace', 'Base', 'Captine']
e = [1000, 10000, ['Ace', 'Base', 'Captine']]
f  = [21.42, 'foobar', 3, 4, 'bark', False, 3.14159]

# 인덱싱
print(">>>>>")
print('d- ', type(d), d)
print('d-  ', d[1])
print('e - ', e[-1][1])
print('e - ', list(e[-1][1])) # str을 list로 변환

# 슬라이싱
print(">>>>>>>")
print('d-  ', d[0:3])
print('d-  ', d[2:])
print('e - ', e[2][1:3])

# 리스트 연산
print(">>>>>>>")
print(c + d)
print(c * 3)
print("'Test' + c[0] - ", 'Test' + str(c[0])) # str로 형변환을 시캬줘야함

# 값 비교
print(c == c[:3] + c[3:])

# 같은 id 값
temp = c  # c를  temp로 할당
print(c == temp)
print(id(temp))
print(id(c))   # 같은 아이디값을 가짐

# 리스트 수정, 삭제
print('>>>>>>')
c[0] = 4
print(c)
c[1:2] = ['a', 'b', 'c'] 
print(c)
c[1:2] = [['a', 'b', 'c']] # 리스트안에 리스트가 들어감
print(c)
c[1] = ['a', 'b', 'c']
print('c - ', c)
c[1:3] = []
print('c - ', c)
del c[3]    # 삭제
print('c - ', c)

# 리스트 함수
a = [5, 2, 3, 1, 4]

print('a - ', a)
a.append(6)
print('a - ', a)
a.sort()          # 오름차순
print('a - ', a)
a.reverse()       # 역순으로 정렬
print('a - ', a)
print('a - ', a.index(5))  # 인데스 번호로 가져옴
a.insert(2, 7)     # 2번째 위치에 7 넣기
print('a - ', a)
a.reverse()
a.remove(1)
print('a - ', a)
print('a - ', a.pop())  # 마지막 인덱스에 있는 것을 뺀다 
print('a - ', a.pop())
print('a - ', a)
print('a - ', a.count(4)) # 4가 몇개 있는지
ex = [8, 9]
a.extend(ex)
print('a - ', a)

# 삭제 remove, pop, del

# 반복문 활용
while a:
    l = a.pop()
    print(2 is l)