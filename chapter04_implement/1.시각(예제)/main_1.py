from sys import stdin as input
input = open('./test/original.txt')

n = int(input.readline())
HOUR_TIME_MAX = 24
MINUTE_TIME_MAX = 60
SECOND_TIME_MAX = 60


def main():
    """  """
    answer = 0
    for hour in range(n + 1):
        for minute in range(MINUTE_TIME_MAX):
            for second in range(SECOND_TIME_MAX):
                if "3" in f"{hour}{minute}{second}":
                    answer += 1
    print(answer)


if __name__ == '__main__':
    main()
