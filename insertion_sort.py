import random
import time
import matplotlib.pyplot as plt

def insertion_sort(arr):

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

if __name__ == "__main__":
    while True:
        try:
            array_size = int(input("Enter the size of array: "))
            if array_size <= 0:
                raise ValueError("Array size must be positive integer.")
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    array = [random.randint(0, 100) for _ in range(array_size)]
    print("Original Array:", array)

    start_time = time.time()
    sorted_insertion = insertion_sort(array.copy())
    end_time = time.time()
    insertion_time = end_time - start_time
    print("Insertion Sort:", sorted_insertion)

    array_sizes = []
    execution_times = []

    for size in range(1, array_size + 1):  
        array = [random.randint(-100, 100) for _ in range(size)]
        start_time = time.time()
        insertion_sort(array.copy())
        end_time = time.time()
        execution_times.append(end_time - start_time)
        array_sizes.append(size)  
        
    plt.plot(array_sizes, execution_times)
    plt.xlabel("Array Size")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Insertion Sort: Execution Time vs. Array Size")
    plt.show()