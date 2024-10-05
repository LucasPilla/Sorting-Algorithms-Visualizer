import time
import threading

def sleepSort(arr, l=0, h=None):
    """
    Improved Sleep Sort Algorithm that correctly sorts the array while yielding intermediate
    states for real-time visualization. Each number "sleeps" for a duration proportional to its value.
    """
    if h is None:
        h = len(arr) - 1

    sorted_result = []  # This will store the sorted numbers in the correct order.

    # Lock to synchronize threads to avoid race conditions
    result_lock = threading.Lock()

    def sleep_and_append(x):
        time.sleep(x * 0.01)  # Sleep for a scaled duration to avoid long waits
        with result_lock:
            sorted_result.append(x)  # Safely append to the result list after waking

    threads = []
    for num in arr[l:h+1]:  # Respecting the range from l to h
        t = threading.Thread(target=lambda: sleep_and_append(num))  # Create thread for each element
        threads.append(t)
        t.start()

    # Wait for all threads to complete
    for t in threads:
        t.join()

    # After all threads are done, sorted_result should be in sorted order
    for i in range(len(sorted_result)):
        arr[i] = sorted_result[i]  # Update the original array with the sorted values
        # Yield the intermediate state of the array for visualization
        yield arr, i, -1, -1, -1  # Yield array and placeholder bar positions

