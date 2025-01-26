import random
import time
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

if __name__ == "__main__":
    while True:
        try:
            array_size = int(input("Enter the size of array: "))
            if array_size <= 0:
                raise ValueError("Array size must be a positive integer.")
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    array = [random.randint(0, 100) for _ in range(array_size)]
    print("Original Array:", array)

    start_time = time.time()
    sorted_bubble = bubble_sort(array.copy())
    end_time = time.time()
    bubble_time = end_time - start_time
    print("Bubble Sort:", sorted_bubble)
    print(f"Bubble Sort Execution Time: {bubble_time:.12f} seconds")

    array_sizes = []
    execution_times = []

    for size in range(1, array_size + 1):
        array = [random.randint(-100, 100) for _ in range(size)]
        start_time = time.time()
        bubble_sort(array.copy())
        end_time = time.time()
        execution_times.append(end_time - start_time)
        array_sizes.append(size)

    plt.plot(array_sizes, execution_times, label="Bubble Sort")
    plt.xlabel("Array Size")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Bubble Sort: Execution Time vs. Array Size")
    plt.legend()
    plt.grid()
    plt.show()
