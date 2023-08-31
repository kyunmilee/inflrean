#chapter 2 - 1
# 01_print 사용법

print('python start!')
print("python start!")
print('''python start!''')
print() #줇 바꿈


#separtator 옵션
print('p', 'y', 't', 'h', 'o', 'n')
print('p', 'y', 't', 'h', 'o', 'n', sep='')
print('p', 'y', 't', 'h', 'o', 'n', sep='|')
# sep= 어떤 것으로 분리가 되어있는지 (원하는 출력으로)
print()


#end 옵션
print('welcome to', end=' ')
print('it news', end=' ')
print('web site', end=' ')
# 끝부분을 어떻게 처리할지
print()


#file 옵션
import sys
print('Learn python', file=sys.stdout)
print()


#format 사용(d-정수, s-문자열, f-실수)
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 'two'))
print('{1} {0}'.format('one', 'two')) # 순서 지정
print()


#%s 사용법
print('%10s' % ('nice')) #10은 10개의 자릿수
print('{:>10}'.format('nice')) # 왼쪽으로 입이 벌어져있어 열자리수 확보
print('{:<10}'.format('nice')) # 오른쪽으로 입이 벌어져있어 열자리수 확보

print('%-10s' % ('nice'))  #-는 왼쪽부터 채움
print('{:10}'.format('nice')) #양수는 오른쪽을 공백으로 채움

print('{:_>10}'.format('nice')) #왼쪽을 _로 채우게 됨
print('{:^10}'.format('nice')) #중앙 정렬

print('%.5s' % ('nice'))
print('%5s' % ('pythonstudy')) # 5개의 자릿수와 상관없이 다 출력
print('%.5s' % ('pythonstudy'))  # .을 찍으면 5개만 출력
print('{:10.5}'.format('pythonstudy')) #10개의 자리를 확보하는데 5개만 출력


# %d 사용법
print('%d %d' % (1, 2))
print('{} {}'.format(1,2))
print('%4d' % (42))
print('{:4d}'.format(42))  # 정수일 경우 d를 붙혀야함 문자는 안붙힘
print()


# %f 사용법
print("%f" % (3.12421521321312312123213123133))  # 1.12f 이면 정수부는 1개 12는 소수부 개수
print('{:f}'.format(42))

print('%06.2f' % (3.141592641234123))   #총 6개 .2는 소수 둘째자리
print('{:06.2f}'.format(3.141592641234123))  #총 6개 .2는 소수 둘째자리


# 추가 print formatting + 자주 나오는 질문
# 3가지 format practices

x = 50
y = 100
text = 308276567
n = 'Lee'
# 출력 1
ex1 = 'n = %s, s= %s, sum=%d' % (n, text, (x + y))
print(ex1)

#출력 2
ex2 = 'n = {n}, s = {s}, sum = {sum}'.format(n = n, s = text, sum = x+y)
print(ex2)

#출력 3
ex3= f'n = {n}, s = {text}, sum={x + y}'
print(ex3)


#구분 기호
m = 100000000
print(f'm = :{m:,}')

#정렬
# ^ : 가운데 정렬, < : 왼쪽 정렬, > : 오른쪽 정렬

t = 20
print(f't : {t:10}')
print(f't : {t:^10}')
print(f't : {t:<10}')
print(f't : {t:>10}')

print()

print(f't : {t:-^10}')