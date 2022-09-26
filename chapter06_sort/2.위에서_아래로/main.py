"""
    위에서 아래로
"""
from sys import stdin as input


class D:
    input = open('./test/original.txt')
    n = int(input.readline())
    numbers = []

    # data sort
    for _ in range(n):
        numbers.append(input.readline().rstrip())
    numbers.sort(reverse=True)


def main():
    """ 함수 실행 """
    print(*D.numbers)

if __name__ == '__main__':
    main()
