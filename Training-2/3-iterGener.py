# 이터레이터 클래스
class Counter:
    def __init__(self, max):
        # 이터레이터의 최대 값 설정
        self.max = max
        # 현재 값을 0으로 초기화
        self.current = 0

    def __iter__(self):
        # __iter__ 메서드는 이터레이터 객체 자체를 반환해야 함
        return self

    def __next__(self):
        # __next__ 메서드는 다음 값을 반환
        if self.current < self.max:
            # 현재 값을 1 증가
            self.current += 1
            # 현재 값을 반환
            return self.current
        else:
            # 현재 값이 최대 값 이상이면 StopIteration 예외 발생
            raise StopIteration

# Counter 클래스의 인스턴스를 생성
counter = Counter(5)

# 이터레이터를 사용하여 값을 반복 출력
for num in counter:
    print(num)

1
2
3
4
5

# 제너레이터 함수
def count_up_to(max):
    # 카운트 초기값을 1로 설정
    count = 1
    # 카운트가 최대 값보다 작거나 같은 동안 반복
    while count <= max:
        # 현재 카운트 값을 반환하고 함수의 실행 상태를 유지
        yield count
        # 카운트를 1 증가
        count += 1

# 제너레이터 객체 생성
counter = count_up_to(5)

# 제너레이터를 사용하여 값을 반복 출력
for num in counter:
    print(num)

1
2
3
4
5


# yield 키워드 -> 제너레이터 함수에서 값을 반환하고 함수의 실행 상태를 일시 중지
def simple_generator():
    yield 1
    yield 2
    yield 3

gen = simple_generator()
print(next(gen))
print(next(gen))
print(next(gen))

1
2
3