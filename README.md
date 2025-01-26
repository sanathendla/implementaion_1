---

## System Specifications
- CPU:Intel Core i7-9700K @ 3.60GHz
- RAM: 16 GB DDR4

---
# Insertion Sort Implementation

This repository provides a Python-based demonstration of the Insertion Sort algorithm. It allows users to input the size of an array, generates random numbers, sorts the array using Insertion Sort, and benchmarks performance for various input sizes. Below, you'll find a detailed breakdown of the algorithm, iterations, and results.

## How It Works
1. Overview of Insertion Sort:
   - Insertion Sort works by progressively building a sorted section of the array. For each new element, it finds the correct position within the sorted portion by comparing it with elements to its left and shifting larger elements.

2. User Input:
   - Users specify the array size, after which the program generates random integers (ranging from 0 to 100) for sorting and benchmarking purposes.

3. Sorting Steps:
   - Detailed Explanation of Iterations:
     - Starting from the second element (index 1), the algorithm compares the current element with elements in the sorted portion.
     - Larger elements in the sorted section are shifted one position to the right.
     - The current element is placed in its correct position.
     - This process continues until the entire array is sorted.

4. Performance Measurement:
   - The program benchmarks execution time for sorting arrays of various sizes, including examples with 12, 82, and 102 elements.
   - A graph is plotted to show the relationship between array size and execution time.

---

## Example Execution
### Input:
```
Enter the size of array: 12
```

### Original Array:
```
[13, 34, 39, 42, 37, 37, 97, 33, 84, 17, 73, 47]
```

### Step-by-Step Iterations:
1. Iteration 1: Place `34` in the correct position.
   - Result: `[13, 34, 39, 42, 37, 37, 97, 33, 84, 17, 73, 47]`
2. Iteration 2: Place `39` in the correct position.
   - Result: `[13, 34, 39, 42, 37, 37, 97, 33, 84, 17, 73, 47]`
3. Iteration 3: Place `42` in the correct position.
   - Result: `[13, 34, 39, 42, 37, 37, 97, 33, 84, 17, 73, 47]`
4. Iteration 4: Place `37` in the correct position.
   - Result: `[13, 34, 37, 39, 42, 37, 97, 33, 84, 17, 73, 47]`
5. Iteration 5: Place `37` in the correct position.
   - Result: `[13, 34, 37, 37, 39, 42, 97, 33, 84, 17, 73, 47]`
6. Iteration 6: Place `97` in the correct position.
   - Result: `[13, 34, 37, 37, 39, 42, 97, 33, 84, 17, 73, 47]`
7. Iteration 7: Place `33` in the correct position.
   - Result: `[13, 33, 34, 37, 37, 39, 42, 97, 84, 17, 73, 47]`
8. Iteration 8: Place `84` in the correct position.
   - Result: `[13, 33, 34, 37, 37, 39, 42, 84, 97, 17, 73, 47]`
9. Iteration 9: Place `17` in the correct position.
   - Result: `[13, 17, 33, 34, 37, 37, 39, 42, 84, 97, 73, 47]`
10. Iteration 10: Place `73` in the correct position.
    - Result: `[13, 17, 33, 34, 37, 37, 39, 42, 73, 84, 97, 47]`
11. Iteration 11: Place `47` in the correct position.
    - Final Sorted Array: `[13, 17, 33, 34, 37, 37, 39, 42, 47, 73, 84, 97]`

### Execution Time for 12 Elements:
```
Insertion Sort Execution Time: 0.000000000000 seconds
```

---

## Visualization
### Graph for Array Sizes of 12, 82, and 102
The graph below illustrates the time taken by Insertion Sort for arrays of different sizes:

1. For Array Size 12:
   - Execution Time: 0.000000 seconds
   - ![image](https://github.com/user-attachments/assets/db9493a0-5011-430a-91d5-ffe2d50a9124)


2. For Array Size 82:
   - Execution Time: 0.0013 seconds
   - ![image](https://github.com/user-attachments/assets/6f174ba6-2065-4113-aebe-fd4d8c83a2ad)

3. For Array Size 102:
   - Execution Time: 0.0018 seconds
   - ![image](https://github.com/user-attachments/assets/49283611-2878-49a4-ade5-6ae601ca38c5)


