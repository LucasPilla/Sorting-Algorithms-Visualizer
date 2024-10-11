import threading
import time


def sleepSort(array, *args):
    sorted_numbers = []
    threads = []

    def add_number(number):
        time.sleep(number * 0.01)  # 放大睡眠时间
        sorted_numbers.append(number)

    for num in array:
        thread = threading.Thread(target=add_number, args=(num,))
        threads.append(thread)
        thread.start()

    # 动态检查并显示排序过程
    while len(sorted_numbers) < len(array):
        temp = sorted(sorted_numbers.copy())  # 当前的已排序部分
        for i in range(len(temp)):
            array[i] = temp[i]
        yield array, len(temp), -1, -1, -1  # 更新显示
        time.sleep(0.01)

    # 完成排序
    for i in range(len(sorted_numbers)):
        array[i] = sorted_numbers[i]
    yield array, -1, -1, -1, set(range(len(array)))  # 绿色条表示完成

