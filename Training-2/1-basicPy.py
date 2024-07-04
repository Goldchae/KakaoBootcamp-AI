# 변수 -> 데이터를 저장하는 메모리 공간에 이름을 붙인 것
x = 10  # 정수형 변수
y = 3.14  # 실수형 변수
name = "Alice"  # 문자열 변수

print(type(x))
print(type(y))
print(type(name))

# <class 'int'>
# <class 'float'>
# <class 'str'>

# 자료형
a = 5  # int
b = 3.2  # float
c = "Hello"  # str
d = True  # bool

print(type(a))
print(type(b))
print(type(c))
print(type(d))

# <class 'int'>
# <class 'float'>
# <class 'str'>
# <class 'bool'>

# 자료형 변환
num_str = "123"
print(type(num_str))
num = int(num_str)  # 문자열을 정수로 변환
print(type(num))
print(num_str)
print(num)

# <class 'str'>
# <class 'int'>
# 123
# 123

# 기본 연산
a = 10
b = 3
print(a + b)  # 덧셈
print(a > b)  # 비교 연산
print(a > 5 and b < 5)  # 논리 연산

# 13
# True
# True

# 조건문
age = 20
if age < 18:
    print("미성년자")
elif age == 18:
    print("갓 성인")
else:
    print("성인")

# 성인

# for 문 -> 리스트, 튜플 등 시퀀스 자료형의 요소를 반복
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# apple
# banana
# cherry


# for 문과 range() 함수 -> 정해진 횟수만큼 반복
for i in range(5):
    print(i)

# 0
# 1
# 2
# 3
# 4

# while 문 -> 조건이 참인 동안 반복
count = 0
while True:
    print(count)
    count += 1
    if count == 5:
        break

# 0
# 1
# 2
# 3
# 4

# break -> 반복문을 즉시 종료, continue -> 현재 반복을 건너뛰고 다음 반복으로 이동
for i in range(10):
    if i == 5:
        break  # 5에서 반복문 종료
    print(i)
print("*"*10)
for i in range(10):
    if i % 2 == 0:
        continue  # 짝수 건너뛰기
    print(i)

# 0
# 1
# 2
# 3
# 4
# **********
# 1
# 3
# 5
# 7
# 9


# 함수
"""
def 함수이름(매개변수):
    코드 블록
    return 반환값
"""
def greet(name):
    return f"Hello, {name}!"

result = greet("Bob")
print(result)

# Hello, Bob!

# lambda 함수
# lambda 매개변수: 반환값
square = lambda x: x ** 2
print(square(5))

# 25

# map 함수의 인자로 사용
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)

# [1, 4, 9, 16, 25]


# 가변 인자 (*args)
"""
def 함수이름(*args):
    코드 블록
"""
def add(*args):
    return sum(args)

print(add(1, 2, 3, 4))

# 10

# 키워드 가변 인자 (**kwargs)
"""
def 함수이름(**kwargs):
    코드 블록
"""
def introduce(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

introduce(name="Alice", age=30, city="Seoul")

# name: Alice
# age: 30
# city: Seoul

# map 함수, 모든 요소에 함수를 적용하여 새로운 리스트 반환
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)

# filter 함수, 조건에 맞는 요소만 걸러내어 새로운 리스트 반환
numbers = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

# reduce 함수, 모든 요소를 누적하여 단일 값을 반환
from functools import reduce
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)

# [1, 4, 9, 16]
# [2, 4]
# 24