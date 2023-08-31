# chapter03_06
# 집합(set) 특징
# 집합(set) 자료향(순서X, 중복X)

# 선언
a = set()  # 빈 집합
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6])
d = set([1, 2, 'Pen', 'Cap', 'Plate'])
e = {'foo', 'bar', 'baz', 'foo', 'qux'}
f = {42, 'foo', (1, 2, 3), 3.14159}

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)

# 튜플 변환(set -> tuple)
t = tuple(b)
print('t - ', type(t), t)
print('t - ', t[0], t[1:3])

# 리스트 변환
l = list(c)
l2 = list(e)
print('l - ', type(l), l)
print('l - ', l[0], l[1:3])
print('l2 - ', type(l2), l2)

# 길이
print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(len(e))

# 집합 자료형 활용
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print('l - ', s1 & s2)
print('l - ', s1.intersection(s2))  # &의 함수임

print('l - ', s1 | s2)
print('l - ', s1.union(s2))  # 합 집합

print('l - ', s1 - s2)
print('l - ', s1.difference(s2))

# 중복 원소 확인
print('l - ', s1.isdisjoint(s2)) # 교집합이 있으면 false

# 부분 집합 확인
print('l - ', s1.issubset(s2))   # s1이 s2의 부분집합인가  # subset
print('l - ', s1.issuperset(s2)) # superset


# 추가 & 제거
s1 = set([1, 2, 3, 4])
s1.add(5)
print('s1 - ', s1)

s1.remove(2)
print('s1 - ', s1)
# s1.remove(7)

s1.discard(3)  # discard도 지우는 것임 
print('s1 - ', s1)

#s1.discard(7) -->    없는 값을 지우려고해도 오류가 발생하지 않음

# 모두 제거
s1.clear()