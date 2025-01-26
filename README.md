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
   ____________________________________________________________________________________________________________________________

   # Selection Sort Implementation

## How It Works
1. Overview of Selection Sort:
   - Selection Sort scans the unsorted section of the array to locate the smallest element and moves it to the correct position at the beginning of that section.
   - As the algorithm progresses, the sorted portion expands while the unsorted portion contracts, continuing until the entire array is sorted.

2. **User Input:**
   - Users provide the size of the array to be sorted.
   - The program generates a random array of integers (ranging from 0 to 100) to demonstrate the sorting process.

3. Sorting Steps:
   - Detailed Explanation of Iterations:
     - For each position in the array (starting from index 0):
       1. Search for the smallest element in the remaining unsorted portion.
       2. Swap the smallest element with the element at the current position.
       3. Repeat until the entire array is sorted.

4. Performance Measurement:
   - The program benchmarks the execution time for sorting arrays of various sizes, including examples with 12, 82, and 102 elements.
   - A graph is plotted to visualize the relationship between array size and execution time.

---

## Example Execution
### Input:
```
Enter the size of array: 12
```

### Original Array:
```
[29, 10, 14, 37, 13, 45, 56, 24, 12, 5, 8, 30]
```

### Step-by-Step Iterations:
1. Iteration 1: Identify the smallest element (`5`) and place it at the first position by swapping.
   - Result: `[5, 10, 14, 37, 13, 45, 56, 24, 12, 29, 8, 30]`
2. Iteration 2: Search for the smallest element (`8`) in the unsorted section and move it to the second position through swapping.
   - Result: `[5, 8, 14, 37, 13, 45, 56, 24, 12, 29, 10, 30]`
3. Iteration 3: Look for the smallest element (`10`) in the unsorted portion and place it in the third position via swapping.
   - Result: `[5, 8, 10, 37, 13, 45, 56, 24, 12, 29, 14, 30]`
4. Iteration 4: Determine the smallest element (`12`) in the unsorted section and position it at the fourth place through swapping.
   - Result: `[5, 8, 10, 12, 13, 45, 56, 24, 37, 29, 14, 30]`
5. Iteration 5: Locate the smallest element (`13`) in the remaining unsorted part and place it in the fifth position by swapping.
   - Result: `[5, 8, 10, 12, 13, 45, 56, 24, 37, 29, 14, 30]`
6. Iteration 6: Identify the smallest element (`14`) from the unsorted section and swap it to the sixth position.
   - Result: `[5, 8, 10, 12, 13, 14, 56, 24, 37, 29, 45, 30]`
7. Iteration 7: Search for the smallest element (`24`) in the remaining unsorted array and move it to the seventh position.
   - Result: `[5, 8, 10, 12, 13, 14, 24, 56, 37, 29, 45, 30]`
8. Iteration 8: Find the smallest element (`29`) in the unsorted part and place it at the eighth position through swapping.
   - Result: `[5, 8, 10, 12, 13, 14, 24, 29, 37, 56, 45, 30]`
9. Iteration 9: Locate the smallest element (`30`) in the remaining unsorted array and swap it into the ninth position.
   - Result: `[5, 8, 10, 12, 13, 14, 24, 29, 30, 56, 45, 37]`
10. Iteration 10: Identify the smallest element (`37`) in the unsorted section and move it to the tenth position by swapping.
    - Result: `[5, 8, 10, 12, 13, 14, 24, 29, 30, 37, 45, 56]`
11. Iteration 11: Find the smallest element (`45`) in the remaining array and place it in the eleventh position through swapping.
    - Final Sorted Array: `[5, 8, 10, 12, 13, 14, 24, 29, 30, 37, 45, 56]`

### Execution Time for 12 Elements:
```
Selection Sort Execution Time: 0.000000000000 seconds
```

---

## Visualization
### Graph for Array Sizes of 12, 82, and 102
The graph below illustrates the time taken by Selection Sort for arrays of different sizes:

1. For Array Size 12:
   - Execution Time: 0.000000 seconds
   - ![image](https://github.com/user-attachments/assets/839cd5cc-dd1f-4f91-b0f4-506fb9837f8a)


2. For Array Size 82:
   - Execution Time: 0.001005649567 seconds
   - ![image](https://github.com/user-attachments/assets/4709947a-54bb-461f-ac37-c12059b5d42f)


3. For Array Size 102:
   - Execution Time: 0.00997781754 seconds
   - ![image](https://github.com/user-attachments/assets/86d7bf50-86b6-4221-977d-00c2727845a2)

_________________________________________________________________________________________________________________________

# Bubble Sort Implementation

## How It Works
1. Overview of Bubble Sort:
   - Bubble Sort repeatedly compares adjacent elements in the array and swaps them if they are in the wrong order.
   - Larger elements "bubble up" to their correct positions with each pass, reducing the unsorted portion until the entire array is sorted.

2. User Input:
   - Users provide the desired size of the array.
   - A random array is generated with integers ranging from 0 to 100 for the demonstration.

3. Sorting Steps:
   - Detailed Explanation of Iterations:
     - For each pass through the array:
       1. Compare every pair of adjacent elements.
       2. Swap them if the left element is greater than the right element.
       3. With each pass, the largest unsorted element is placed in its correct position.
       4. Repeat until no swaps are needed, indicating the array is fully sorted.
      
4. Performance Measurement:
   - The program benchmarks Bubble Sort's execution time for arrays of different sizes, including examples with 12, 82, and 102 elements.
   - A graph is generated to visualize the relationship between input size and execution time.

---

## Example Execution
### Input:
```
Enter the size of array: 12
```

### Original Array:
```
[34, 12, 25, 9, 78, 45, 56, 33, 15, 10, 50, 5]
```

### Step-by-Step Iterations:
1. Iteration 1: Compare and swap adjacent elements, pushing the largest element (`78`) to the end.
   - Result: `[12, 25, 9, 34, 45, 56, 33, 15, 10, 50, 5, 78]`
2. Iteration 2: Repeat the process for the remaining unsorted section, placing the second largest element (`56`) before `78`.
   - Result: `[12, 9, 25, 34, 33, 45, 15, 10, 50, 5, 56, 78]`
3. Iteration 3: Continue comparing and swapping, moving the next largest element (`50`) to its position.
   - Result: `[9, 12, 25, 33, 34, 15, 10, 45, 5, 50, 56, 78]`
4. Iteration 4: Push the next largest element (`45`) to its correct spot.
   - Result: `[9, 12, 25, 33, 15, 10, 5, 34, 45, 50, 56, 78]`
5. Iteration 5: Move the next largest element (`34`) into its position.
   - Result: `[9, 12, 25, 15, 10, 5, 33, 34, 45, 50, 56, 78]`
6. Iteration 6: Continue until no more swaps are needed, leaving the array sorted.
   - Final Sorted Array: `[5, 9, 10, 12, 15, 25, 33, 34, 45, 50, 56, 78]`

### Execution Time for 12 Elements:
```
Bubble Sort Execution Time: 0.000005 seconds
```

---

## Visualization
### Graph for Array Sizes of 12, 82, and 102
The graph below illustrates the time taken by Bubble Sort for arrays of different sizes:

1. **For Array Size 12:**
   - Execution Time: 0.000000000000 seconds
   - ![image](https://github.com/user-attachments/assets/ccf3fbfb-ce6d-4cfd-b8b5-86bf437cb69f)


2. **For Array Size 82:**
   - Execution Time: 0.000998020172 seconds
   - ![image](https://github.com/user-attachments/assets/1eeb8fb3-8c92-4e23-8e99-1b2d65c029ed)


3. **For Array Size 102:**
   - Execution Time: Time: 0.001036882401 seconds
   - ![image](https://github.com/user-attachments/assets/16db7af3-c731-4d72-8829-f017e92ef309)
  
   _______________________________________________________________________________________________________________
## Conclusion

Through a series of experiments, it’s clear that Insertion Sort is the most efficient and practical choice for sorting small to medium-sized datasets. It excels at handling partially sorted arrays, thanks to its straightforward approach of placing each element in its correct position with minimal swaps. This makes it faster and more suitable for situations where datasets are relatively small or nearly sorted.

Selection Sort, on the other hand, is simple and reliable. It works by consistently finding the smallest element from the unsorted portion and placing it in its correct position. However, this method doesn’t take advantage of partially sorted data, which makes it slower compared to Insertion Sort in most practical scenarios. Despite its predictability and ease of implementation, it’s less efficient when time is a critical factor.

Bubble Sort, although easy to understand and implement, is the least efficient of the three. It requires numerous swaps to place elements in order, which significantly slows it down. Even with optimized versions, Bubble Sort struggles to match the speed and efficiency of Insertion Sort and Selection Sort. Its use is primarily limited to educational purposes, where simplicity in explaining sorting concepts is more important than performance.

Hence, Insertion Sort is the best option when speed and practicality are key, particularly for small and moderately sized datasets. Selection Sort can be a viable alternative in situations where simplicity and low memory usage are essential. However, Bubble Sort is not suitable for most real-world scenarios and is better reserved as a learning tool. For larger datasets, more advanced algorithms like Quick Sort or Merge Sort should be considered for their superior performance and scalability.






