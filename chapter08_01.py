# chapter08_01
# 파이썬 내장(Built-in) 함수
# 자주 사용하는 함수 위주로 실습
# 사용하다보면 자연스럽게 숙달
# str(), int(), tuple() 형변환 이미 학습

# 절댓값
# abs()
print(abs(-3))

print('-' * 19)

# all, any : iterable 요소 검사(참, 거짓)
print(all([1,2,3])) # and  # 하나라도 false면 0이 나온다
print(any([1,2,0])) # or  # 하나라도 true가 있으면 true가 나온다

print('-' * 19)

# chr : 아스키 -> 문자 , ord : 문자 -> 아스키
print(chr(67))
print(ord('C'))

print('-' * 19)

# enumerate : 인덱스 + Iterable 객체 생성
for i, name in enumerate(['abc', 'bcd', 'efg']):
    print(i, name)

print('-' * 19)

#  filter : 반복가능한 객체 요소를 지정한 함수 조건에 맞는 값 추출

def conv_pos(x):
    return abs(x) > 2
    
print(list(filter(conv_pos, [1, -3, 2, 0, -5, 6])))
print(list(filter(lambda x: abs(x) > 2, [1, -3, 2, 0, -5, 6])))

print('-' * 19)

# id : 객체의 주소값(레퍼런스) 반환

print(id(int(5)))
print(id(4))

print('-' * 19)

# len : 요소의 길이 반환
print(len('abcdefg'))
print(len([1,2,3,4,5,6,7]))

print('-' * 19)

# max, min : 최대값, 최소값

print(max([1,2,3]))
print(max('python study'))
print(min([1,2,3]))
print(min('python study'))  # 최솟값 공백

print('-' * 19)

# map : 반복가능한 객체 요소를 지정한 함수 실행 후 추출
def conv_abs(x):
    return abs(x)
    
print(list(map(conv_abs,[1,-3,2,0,-5,6])))
print(list(map(lambda x:abs(x),[1,-3,2,0,-5,6])))

print('-' * 19)

# pow : 제곱값 반환
print(pow(2,10))

print('-' * 19)

# range : 반복가능한 객체(Iterable) 반환
print(range(1,10,2))
print(list(range(1,10,2)))
print(list(range(0,-15,-1)))

print('-' * 19)

# round : 반올림
print(round(6.5781, 2))   # 둘째자리에서 반올림
print(round(5.6))         # 첫째자리에서 반올림

print('-' * 19)

# sorted : 반복가능한 객체(Iterable) 정렬 후 반환 
print(sorted([6,7,4,3,1,2]))
a = sorted([6,7,4,3,1,2])
print(a)
print(sorted(['p','y','t','h','o','n']))  # 알파벳 순서대로

print('-' * 19)

# sum : 반복가능한 객체(Iterable) 합 반환
print(sum([6,7,8,9,10]))
print(sum(range(1,101)))

print('-' * 19)

# type : 자료형 확인
print(type(3))
print(type({}))
print(type(()))
print(type([]))

print('-' * 19)

# zip : 반복가능한 객체(Iterable)의 요소를 묶어서 반환
print(list(zip([10,20,30],[40,50,777])))   # 짝이 없으면 봔환 불가능
print(type(list(zip([10,20,30],[40,50,777]))[0]))