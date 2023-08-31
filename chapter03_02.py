#chapter 03_02

# 빈 문자열
str_t1 = ''
str_t2 = str()

print(type(str_t1), len(str_t1))
print(type(str_t2), len(str_t2))

# 이스케이프 문자 사용

print("I\'m Boy")
# \n : 개행
# \t : 탭
# \\ : 문자
# \' : 문자
# \" : 문자
# \000 : 널 문자

escape_str1 = "Do you have a \"retro games\"?"
escape_str2 = 'What\'s on TV?'


# 출력1
print(escape_str1)
print(escape_str2)

# row string
raw_s1 = r'D:\python\test'
print(raw_s1)
print()

# 멀티 라인 입력
multi_str = \
'''
string
multi line
test
'''
# \를 넣어주면 어떤 변수를 바인딩 한다고 생각, # 역슬러쉬 사용

# 문자열 연산
str_o1 = "Python"
str_o2 = "Apple"
str_o3 = "How are you doing?"
str_o4 = "Seoul Deajeon Busan Jinju"

print(str_o1 * 3)
print(str_o1 + str_o2)
print('y' in str_o1)  # str_o1에 y가 포함되어 있는지 in
print('n' in str_o1)
print('P' not in str_o2) # not in 


# 문자열 형 변환
print(str(66), type(str(66))) # 문자열의 66이다
print(str(10.1), type(str(10.1)))
print(str(True), type(str(True)))

# 문자열 함수(upper, isalnum, startswith, count, endswith, isalpha)
print("Capitalize", str_o1.capitalize()) # 첫글자를 대문자로 변환
print("endswith", str_o2.endswith("e"))  # 마지막이 e로 끝나는지
print("replace", str_o1.replace("thon", "Good")) # thon을 Good으로 변환해줌
print("sorted", sorted(str_o1)) # 정렬해서 리스트 형태로 변환
print("split", str_o4.split(" ")) # 공백을 기준으로 리스트 형태로 바꿔줌

# 반복 (시퀀스) 
im_str = "Good Boy!"
print(dir(im_str))  # __iter__

# 출력
for i in im_str:
    print(i)

# 슬라이싱
str_s1 = "Nice Python"

# 슬라이싱 연습
print(str_s1[0:3]) # 0 1 2 가 나옴
print(str_s1[5:]) # 5부터 끝까지
print(str_s1[:len(str_s1)]) # 처음부터 길이만큼
print(str_s1[:len(str_s1) - 1]) 
print(str_s1[1:4:2]) # 두 칸씩 건너뜀
print(str_s1[-5:])
print(str_s1[1:-2])
print(str_s1[::-1]) # 오른쪽에서 왼쪽으로

# 아스키 코드(또는 유니코드)
a = 'z'
print(ord(a)) # ord는 아스키 숫자 값을 알려줌
print(chr(122)) #chr은 위에거 반대

