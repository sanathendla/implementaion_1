System Specifications
**CPU: ** Intel Core i7-9700K @ 3.60GHz

**RAM: ** 16 GB DDR4

Insertion Sort Implementation
This repository contains an Insertion Sort (Python-based) algorithm. It permits the definition of the array size, generation of random numbers, and sorting of an array via Insertion Sort, as well as performance benchmarking for a family of array sizes. Appended is a description of the algorithm, number of iterations and output.

How It Works
**Overview of Insertion Sort: **
Insertion Sort is implemented iteratively in a way such that the partially sorted array is built from bottom up. In case of all newly introduced elements, it precisely locates the element in the ordered region by comparing it with other left neighbors and by progressively moving all larger neighbor to the right.

**User Input: **
The size of the array (i.e., the maximum number of elements allowed in the array) is defined by the user and program, then integer values from the set [0,100) are randomly generated and used for array manipulation, benchmarking, and sorting.

**Sorting Steps: **
**Detailed Explanation of Iterations: **
The transformation algorithm, according to the second (index 1) the elementwise comparison between elements of the algorithmic part and those of the ordered part is carried out.

Larger items are shifted to the right position by one position if they are present.

The element is now in its correct location.

This process repeats until the sorted array is obtained.

**Performance Measurement: **
The scheme relates the time to generate an array of varying sizes, the sizes of arrays whose element have to be generated are 12, 82 and 102.

The relationship between array size and time to process has been represented by drawing a graph.

Example Execution
Input: ### Input:
 Copy

Enter the size of array: 12
Original Array: ### Original Array:
 Copy

[13, 34, 39, 42, 37, 37, 97, 33, 84, 17, 73, 47].
Step-by-Step Iterations: ### Step-by-Step Iterations:
**Iteration 1: ** Place 34 in the correct position.
Result: [13, 34, 39, 42, 37, 37, 97, 33, 84, 17, 73, 47].
**Iteration 2: ** Place 39 in the correct position.
Result: [13, 34, 39, 42, 37, 37, 97, 33, 84, 17, 73, 47].
**Iteration 3: ** Place 42 in the correct position.
Result: [13, 34, 39, 42, 37, 37, 97, 33, 84, 17, 73, 47] .
**Iteration 4: ** Place 37 in the correct position.
Result: [13, 34, 37, 39, 42, 37, 97, 33, 84, 17, 73, 47] .
**Iteration 5: ** Place 37 in the correct position.
Result: [13, 34, 37, 37, 39, 42, 97, 33, 84, 17, 73, 47] .
**Iteration 6: ** Place 97 in the correct position.
Result: [13, 34, 37, 37, 39, 42, 97, 33, 84, 17, 73, 47].
**Iteration 7: ** Place 33 in the correct position.
Result: [13, 33, 34, 37, 37, 39, 42, 97, 84, 17, 73, 47] .
**Iteration 8: ** Place 84 in the correct position.
Result: It is comprised of 13, 33, 34, 37, 37, 39, 42, 84, 97, 17, 73, 47] (e.g., M1 maps order the systems from lowest precision (C1) to highest precision (C13).
**Iteration 9: ** Place 17 in the correct position.
Result: 13, 17, 33, 34, 37, 37, 39, 42, 84, 97, 73, 47 .
**Iteration 10: ** Place 73 in the correct position.
Result: 13, 17, 33, 34, 37, 37, 39, 42, 73, 84, 97, 47.
**Iteration 11: ** Place 47 in the correct position.
Final Sorted Array: Range 13, 17, 33, 34, 37, 37, 39, 42, 47, 73, 84, 97.
Execution Time for 12 Elements: ### Execution Time for 12 Elements:
 Copy

Insertion Sort Execution Time: 0.000000000000 seconds
Visualization
Graph of array sizes of 12, 82 and 102.

The following figure shows the number of seconds needed to perform the Insertion Sort operations on sizes as arrays.

**For Array Size 12: **
Execution Time: 0.000000 seconds

![image](https: //github.com/user-attachments/assets/9946c58f-5596-4be7-a0be-a2274391ea74)

**For Array Size 82: **
Execution Time: 0.0010 seconds

![image](https: //github.com/user-attachments/assets/ae60a189-4013-41ba-becb-873a39c66906)

**For Array Size 102: **
Execution Time: 0.0014 seconds

![image](https: //github.com/user-attachments/assets/41cd33d0-9d94-4d15-abd8-1549637452ac)
