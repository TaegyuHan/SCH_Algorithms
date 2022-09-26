import random


def select_sort(array: list[int]) -> None:
    """ 선택 정렬 """
    for idx1 in range(len(array)):
        min_idx = idx1
        for idx2 in range(idx1 + 1, len(array)):
            if array[idx2] < array[min_idx]:
                min_idx = idx2
        array[idx1], array[min_idx] = array[min_idx], array[idx1]
    return array


def selection_sort(array, size):
    for ind in range(size):
        min_index = ind

        for j in range(ind + 1, size):
            # select the minimum element in every iteration
            if array[j] < array[min_index]:
                min_index = j
        # swapping the elements to sort the array
        (array[ind], array[min_index]) = (array[min_index], array[ind])

    return array


def insert_sort(array: list[int]) -> None:
    """ 삽입 정렬 """
    for idx1 in range(1, len(array)):
        tmp = array.pop(idx1)
        find = False
        for idx2 in range(idx1):
            if tmp <= array[idx2]:
                array.insert(idx2, tmp)
                find = True
                break
        if not find:
            array.insert(idx1, tmp)
    return array

def insertion_sort(arr):
    for end in range(1, len(arr)):
        for i in range(end, 0, -1):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]

def quick_sort(array: list[int]) -> None:
    """ 퀵 정렬 """


if __name__ == '__main__':
    """ 실행 """
    # number = [random.randrange(0, 10) for _ in range(10)]
    number = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    # select_sort(array=number)
    # insert_sort(array=number)
    #
