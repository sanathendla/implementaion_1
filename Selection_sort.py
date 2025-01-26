import random
import time
import matplotlib.pyplot as plt

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
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
    sorted_selection = selection_sort(array.copy())
    end_time = time.time()
    selection_time = end_time - start_time
    print("Selection Sort:", sorted_selection)
    print(f"Selection Sort Execution Time: {selection_time:.12f} seconds")

    array_sizes = []
    execution_times = []

    for size in range(1, array_size + 1):
        array = [random.randint(0, 100) for _ in range(size)]
        start_time = time.time()
        selection_sort(array.copy())
        end_time = time.time()
        execution_times.append(end_time - start_time)
        array_sizes.append(size)

    plt.plot(array_sizes, execution_times, label="Selection Sort")
    plt.xlabel("Array Size")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Selection Sort: Execution Time vs. Array Size")
    plt.legend()
    plt.grid()
    plt.show()