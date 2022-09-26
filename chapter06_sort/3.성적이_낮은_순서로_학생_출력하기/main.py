"""
    성적이 낮은 순서로 학생 출력하기
"""
from sys import stdin as input


class D:
    input = open('./test/original.txt', encoding="utf-8")
    n = int(input.readline())
    members = []

    # data sort
    for _ in range(n):
        members.append(input.readline().split())
    members.sort(key=lambda x: x[1])


def main():
    """ 함수 실행 """
    print(*map(lambda x: x[0], D.members))


if __name__ == '__main__':
    main()
