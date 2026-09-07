### Heaps

A **Heap** is a specialized tree-based data structure that satisfies the **Heap Property**:

* **Max-Heap:** The value of each node is less than or equal to the value of its parent (A[parent (i)] >= A[i]). The
  maximum element is always at the root.
* **Min-Heap:** The value of each node is greater than or equal to the value of its parent (A[parent (i)] <= A[i]). The
  minimum element is always at the root.

It is typically implemented as a **Binary Heap** laid out contiguously inside an array, providing optimal CPU cache
locality with standard implicit pointer arithmetic for indexing:

* Left Child: 2i + 1
* Right Child: 2i + 2
* Parent: (i - 1) / 2

### Time & Space Complexity

| Operation                      | Time Complexity    | Space Complexity |
|--------------------------------|--------------------|------------------|
| **Get Min / Max (Peek)**       | O(1)               | O(1)             |
| **Insert (Push)**              | O(log N) amortized | O(1)             |
| **Extract Min / Max (Pop)**    | O(log N)           | O(1)             |
| **Heapify (Build from array)** | O(N)               | O(1) in-place    |

### When to Use

* **Priority Queue Implementations:** Scheduling tasks dynamically based on execution deadlines or priority values.
* **Streaming Top-K Tracking:** Maintaining the K largest or smallest elements from a continuous data stream without
  sorting the entire dataset (O (N \log K) runtime using an O (K) bounded heap).
* **Graph Algorithms:** Optimizing greedy pathfinding algorithms like **Dijkstra's** (O ((V + E) \log V)) or **Prim's**
  minimum spanning tree algorithm.
* **In-Place Sorting (Heapsort):** Sorting datasets in strictly O (N \log N) time with O (1) auxiliary space guarantees
  (eliminating O (N) recursion allocation overhead found in QuickSort/MergeSort worst-case bounds).
* **Median Maintenance:** Using a two-heap approach (a Max-Heap for the lower half and a Min-Heap for the upper half) to
  compute streaming medians in O (1) time per query.