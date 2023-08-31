# chapter03_05
# 파이썬 딕션너리 
# 딕샤너리 자료형(순서X, 키 중복X, 수정O, 삭제O)

# 산안
a = {'name': 'Kim', 'phone': '01012345678', 'birth': '870124'}
b = {0: 'Hello python!'}   # 키는 숫자로도 선언 가능
c = {'arr': [1, 2, 3, 4]}  # 값은 리스트 형태도 가능
d = {
	 'Name' : 'Niceman',
	 'City'   : 'Seoul',
	 'Age': '33',
	 'Grade': 'A',
	 'Status'  : True
}
e =  dict([
	 ( 'Name', 'Niceman'),
	 ('City', 'Seoul'),
	 ('Age', '33'),
	 ('Grade', 'A'),
	 ('Status', True)
])                         # 튜플로도 가능

f =  dict(
	 Name='Niceman',
	 City='Seoul',
	 Age='33',
	 Grade='A',
	 Status=True
)

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(c), e)
print('f - ', type(c), f)

# 출력
print('a - ', a['name'])  # 존재X -> 에러 발생
print('a - ', a.get('name'))  # 존재X -> None 처리
print('b - ', b[0])
print('b - ', b.get(0))
print('c - ', c['arr'])
print('c - ', c['arr'][3])
print('c - ', c.get('arr'))
print('d - ', d.get('Age'))
print('e - ', e.get('Grade'))
print('f - ', f.get('City'))

# 딕셔너리 추가
a['address'] = 'seoul'    # 만약 키 값이 같으면 그 깂을 수정
print('a - ', a)
a['rank'] = [1, 2, 3]
print('a - ', a)

# 딕셔너리 길이
print(len(a))
print(len(b))
print(len(d))
print(len(e))

# dict_keys, dict_values, dict_items : 반복문(iterate) 사용 가능

# 키 값들만 가져온다
print('a - ', a.keys())         
print('b - ', b.keys())
print('c - ', c.keys())
print('d - ', d.keys())

# 리스트 형태로 키 변환
print('a - ', list(a.keys()))
print('b - ', list(b.keys()))
print('c - ', list(c.keys()))
print('d - ', list(d.keys()))

# 값만 리스트 형태로
print('a - ', a.values())
print('b - ', b.values())
print('c - ', c.values())
print('d - ', d.values())

print('a - ', list(a.values()))
print('b - ', list(b.values()))
print('c - ', list(c.values()))
print('d - ', list(d.values()))

# 키와 값이 하나의 튜블로 리스트로 둘러싸여서져서 나옴
print('a - ', a.items())
print('b - ', b.items())
print('c - ', c.items())
print('d - ', d.items())

# pop으로 꺼내오고 없앰
print('a - ', a.pop('name'))
print('b - ', b.pop(0))
print('c - ', c.pop('arr'))
print('d - ', d.pop('City'))

# 임의로 하나를 선택해서 없앰
print('f - ', f.popitem())
print('f - ', f.popitem())
print('f - ', f.popitem())
print('f - ', f.popitem())
print('f - ', f.popitem())
# 예외
# print('f - ', f.popitem())

print('a - ', 'name' in a)
print('a - ', 'addr' in a)

# 수정
f.update(Age=36)

temp = {'Age': 27}

print('f - ', f)

f.update(temp)

print('f - ', f)