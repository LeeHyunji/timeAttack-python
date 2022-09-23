# Q3. filter/map 혹은 리스트 축약식 활용해서 리스트 다뤄보기
#
# 아래 문제를 filter와 map 함수 혹은 리스트 축약식을 활용해 풀어주세요
# 1. 1부터 10000까지의 숫자를 `numbers` 변수에 할당해주세요
# 2. 1부터 10000까지 숫자 중, 짝수에 해당하는 숫자만 `even_numbers` 변수에 할당해주세요
# 3. 1부터 10000까지의 숫자 중, 3의 배수이며 15의 배수가 아닌 숫자에 10을 곱하여 `some_numbers` 에 할당해주세요

def get_even_numbers(numbers):
    result = list(filter(lambda x: x % 2 == 0, numbers))
    # some code
    return result


def get_some_numbers(numbers):
    filter_numbers = list(
        filter(lambda x: (x % 3 == 0) & (x % 5 != 0), numbers))
    result = list(map(lambda x: x*10, filter_numbers))
    # some code
    return result


def main():
    numbers = [i+1 for i in range(1000)]   # 1 ~ 10000
    even_numbers = get_even_numbers(numbers)
    some_numbers = get_some_numbers(numbers)
    print(even_numbers)  # [2, 4, 6, ...]
    print(some_numbers)  # [30, 60, 90, 120, 180, ...]


main()
