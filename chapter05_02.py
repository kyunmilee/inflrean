# chapter05_02
# 파이썬 사용자 입력
# *** 기본 타입은 무조건 str ***

# 예제1
name = input("Enter Your Name : ")
grade = input("Enter Your Grade : ")
company = input("Enter Your Company name : ")

print(name, grade, company)

# 예제2
number = input("Enter number : ")
name = input("Enter name : ")

print("type of number", type(number), number * 3)
print("type of nanme", type(name))

# 예제3(계산)
first_number = int(input("Enter number1 : "))
second_number = int(input("Enter number2 : "))

total = first_number + second_number
print("first_number + second_number : ", total)

# 예제4
float_number = float(input("Enter a float number : "))

print("input float : ", float_number)
print("input type : ", type(float_number))

# 예제5
print("FirstName - {0}, LastName - {1}".format(input("Enter first name : "), input("Enter second name : ")))


# 예제1 -> 예외처리
# try:
#     n = int(input('Enter a number: '))
#     print('OK. Your number is: ', n)

# except ValueError:
#     print('This is not a number.')

# 예제2 -> 올바른 값 입력 완료 까지 지속
# while True:
#     try:
#         n = int(input('Enter a number: '))
#         break
    
#     except ValueError:
#         print('This is not a number. Try again.')
        
# print('OK. Your number is: ', n)