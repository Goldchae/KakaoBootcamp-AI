# 클래스 -> 객체를 정의하는 데 사용되는 청사진
"""
class 클래스이름:
    def __init__(self, 매개변수):
        self.속성 = 매개변수

    def 메서드이름(self, 매개변수):
        코드 블록
"""
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return "Woof!"

# 인스턴스 생성
my_dog = Dog("Buddy", 3)
print(my_dog.name)
print(my_dog.bark())

# Buddy
# Woof!


# 상속 -> 기존 클래스(부모 클래스)를 기반으로 새로운 클래스(자식 클래스)를 정의하는 것
"""
class 부모클래스:
    # 부모 클래스의 속성과 메서드 정의

class 자식클래스(부모클래스):
    # 자식 클래스의 속성과 메서드 정의
"""
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method") #에러던지기

class Dog(Animal): # Animal 상속
    def speak(self):
        return "Woof!"

class Cat(Animal): # Animal 상속
    def speak(self):
        return "Meow!"
    


# 다형성 -> 동일한 인터페이스를 사용하여 서로 다른 데이터 타입의 객체를 다룰 수 있는 능력

animals = [Dog("Buddy"), Cat("Whiskers")]
for animal in animals:
    print(f"{animal.name} says {animal.speak()}")

# Buddy says Woof!
# Whiskers says Meow!


# 매직 메서드 (Magic Methods) -> 파이썬이 내부적으로 사용하는 메서드
"""
__init__: 객체 초기화 메서드
__str__: 객체의 문자열 표현을 반환
__repr__: 객체의 공식 문자열 표현을 반환
"""
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __repr__(self):
        return f"Book({self.title}, {self.author})"

my_book = Book("1984", "George Orwell")
print(str(my_book))
print(repr(my_book))

# 1984 by George Orwell
# Book(1984, George Orwell)


# 연산자 오버로딩 -> 파이썬의 기본 연산자를 사용자 정의 클래스에서 사용할 수 있도록 메서드를 정의
"""
__add__: + 연산자
__sub__: - 연산자
__mul__: * 연산자
__truediv__: / 연산자
"""
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(5, 7)
v3 = v1 + v2
print(v3)

# Vector(7, 10)