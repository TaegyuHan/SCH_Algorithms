import os
import time
from collections.abc import Generator

import pandas
import pandas as pd


def time_check(func):
    """ 시간 확인하기 """

    def wrapper_function(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        return end_time - start_time, result

    return wrapper_function


def test_files(dir_path: str) -> Generator[str]:
    """ 테스트 케이스 불러오기 """
    for (root, directories, files) in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            yield file_path


def result_df(solutions) -> pandas.core.frame.DataFrame:
    """ 문제 풀이 결과 출력하기 """
    solution_col = []
    time_col = []
    result_col = []
    test_file_path_col = []

    for file_path in test_files(dir_path="test"):
        for i, solution in enumerate(solutions):
            with open(file_path, "r") as test:
                time, result = solution(test=test)
                if i == 0: i = "ansmwer"
                solution_col.append(f"{i}")
                time_col.append(time)
                result_col.append(result)
                test_file_path_col.append(file_path)

    d = {
        'solution_n': solution_col,
        'time': time_col,
        'result': result_col,
        'test_file_path': test_file_path_col
    }

    return pd.DataFrame(data=d)
