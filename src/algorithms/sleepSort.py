import threading
import time

# Function to perform sleep sort
def sleep_sort(numbers):
    
    # Nested function that sleeps for 'n' seconds and prints 'n'
    def sleep_and_print(n):
        # Sleep for 'n' seconds (simulating sorting delay based on value)
        time.sleep(n)
        # Print the number after sleeping (in sorted order based on sleep time)
        print(n, end=" ")

    # List to keep track of the threads
    threads = []

    # Create and start a thread for each number in the input list
    for num in numbers:
        # Create a thread that runs 'sleep_and_print' for each number
        thread = threading.Thread(target=sleep_and_print, args=(num,))
        # Append the thread to the list of threads
        threads.append(thread)
        # Start the thread
        thread.start()

    # Ensure all threads complete before the function ends
    for thread in threads:
        # Wait for each thread to finish execution (join means waiting for the thread)
        thread.join()