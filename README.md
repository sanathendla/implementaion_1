# Insertion Sort Implementation

This is a Python implementation of the Insertion Sort algorithm. Users can input an array size, it will then create random numbers, sort that array with Insertion Sort, and measure the performance for a few sizes.

Here is the algorithm explanation, iteration, and result:

---
## How It Works
1. **What is Insertion Sort:**
- Insertion Sort works by maintaining a sorted portion of the array. For each new element, it locates the proper place for it among the elements to its left using comparisons and shifting larger elements.

2. **User Input:**
   - Users are asked for the size of the array. On input, the program comes up with random integers between 0 and 100, which are used to generate the benchmark.

3. **Iteration Steps:**
   - Iteration Steps are explained in detail
     - Starting from the second element at index 1, it compares the current element with elements of the sorted section.
     - Elements greater than the current element in the sorted section are moved one position right.
     - The current element is placed at its correct position.
- This process goes on until the whole array gets sorted.

4. **Performance Evaluation:**
   - The code measures the running time for the sorting of different sizes of arrays, such as 12, 82, and 102 elements.
   - A graph is drawn to indicate the trend of array size and running time.

---

## Running the Code
### Input:
```
Enter the size of array: 12
```

### Original Array:
```
[13, 34, 39, 42, 37, 37, 97, 33, 84, 17, 73, 47]
 
### Iteration Steps:
1. **Step 1:** Put `34` in its proper place.
  - Output: `[13, 34, 39, 42, 37, 37, 97, 33, 84, 17, 73, 47]`
2. **Step 2:** Put `39` in its proper place.
  - Output: `[13, 34, 39, 42, 37, 37, 97, 33, 84, 17, 73, 47]`
3. **Round 3:** Put `42` in right place.
   - Output: `[13, 34, 39, 42, 37, 37, 97, 33, 84, 17, 73, 47]`
4. **Round 4:** Put `37` in right place.
   - Output: `[13, 34, 37, 39, 42, 37, 97, 33, 84, 17, 73, 47]`
5. **Round 5:** Put `37` in right place.
- Output: `[13, 34, 37, 37, 39, 42, 97, 33, 84, 17, 73, 47]`
6. **Step 6:** Put `97` at the correct position.
   - Output: `[13, 34, 37, 37, 39, 42, 97, 33, 84, 17, 73, 47]`
7. **Step 7:** Put `33` at the correct position.
   - Output: `[13, 33, 34, 37, 37, 39, 42, 97, 84, 17, 73, 47]`
8. Iteration 8: Place `84`
       Output: `[13, 33, 34, 37, 37, 39, 42, 84, 97, 17, 73, 47]`.
9. Iteration 9: Place `17`.
         Output: `[13, 17, 33, 34, 37, 37, 39, 42, 84, 97, 73, 47]`.
10. Iteration 10: Place `73` in proper location.
- Output: `[13, 17, 33, 34, 37, 37, 39, 42, 73, 84, 97, 47]`
11. **Iteration 11:** Insert `47` at appropriate position.
    - Final Sorted Array: `[13, 17, 33, 34, 37, 37, 39, 42, 47, 73, 84, 97]`

### Time Complexity for 12 Elements:
```
Insertion Sort Time Complexity: 0.000000000000 seconds
```

---

## Graph
### Graph for 12, 82, and 102 Elements
The following graph shows the time taken by Insertion Sort for different sizes of arrays:

1. **For Array Size 12:** 
   - Execution Time: 0.000000 seconds
   - 
2. **For Array Size 82:** 
   - Execution Time: 0.000015 seconds
   -
3. **For Array Size 102:** 
   - Execution Time: 0.000025 seconds
   -

