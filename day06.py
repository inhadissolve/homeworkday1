# def factorial_repetition(n) -> int:
#     '''
#     반복문을 이용한 팩토리얼 함수
#     :param n: 정수, int
#     :return: 팩토리얼 값, int
#     '''
#     result = 1
#     for i in range(2, n+1):
#         result = result * i
#     return result
#
# def factorial_recursion(n):
#     '''
#     재귀함수를 사용한 팩토리얼 함수
#     :param n: 정수, int
#     :return: function, int
#     '''
#     if n == 1:
#         return n
#     else:
#         return n * factorial_recursion(n-1)
#
# number = int(input("number : "))
# print(factorial_repetition(number))
# print(factorial_recursion(number))
# print(globals())


# 한수를 입력받고 피보나치 값 출력하기
"""
피보나치 수 계산 함수(재귀함수 버전)
:param n:
:return: 피보나치 계산 결과 값
"""

def fibonacci_recursion(n) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursion(n-2) + fibonacci_recursion(n-1)


for i in range(10):
    print(fibonacci_recursion(i), end=" ")

print("\n")


def fibonacci_loop(n) -> int:
    n_list=[0,1]
    for i in range(n+1):
        n_list.append(n_list[i] + n_list[i + 1])

    return n_list[n]

for i in range(10):
    print(fibonacci_loop(i), end=" ")