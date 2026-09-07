### Stack

A **Stack** is a linear data structure that operates on a **Last-In, First-Out (LIFO)** policy: the last element added
to the stack is the first one to be removed.

```
                  [ LIFO Stack Structure ]

       Push (Insert) ──┐              ┌── Pop / Peek (Remove/Inspect)
                       ▼              │
                   ┌───────┐ ◄────────┘
                   │ Top   │ (Element N)
                   ├───────┤
                   │       │ (Element N-1)
                   ├───────┤
                   │       │ ...
                   ├───────┤
                   │ Bottom│ (Element 1)
                   └───────┘

```

---

### Memory Layout & Complexity

Stacks are typically implemented over contiguous dynamic arrays (`list` in Python, `std::vector` in C++, `Vec` in Rust)
or singly linked lists. Array-backed stacks leverage CPU cache prefetching and guarantee amortized O (1) operations at
the contiguous boundary.

| Operation      | Time Complexity | Memory Impact                                         |
|----------------|-----------------|-------------------------------------------------------|
| **Push**       | O(1) amortized  | Contiguous heap expansion (or single node allocation) |
| **Pop**        | O(1)            | Boundary index decrement (zero reallocations)         |
| **Peek / Top** | O(1)            | O(1) stack/array pointer offset reading               |

---

### When to Use

1. **Call Stack & Recursion Management:**

* Tracking function execution contexts, local variables, and return addresses during nested function calls or recursion.


2. **Expression Evaluation & Parsing:**

* Converting and evaluating mathematical expressions (Infix to Postfix/Prefix using Dijkstra's Shunting-yard algorithm).
* Matching balanced delimiters (brackets, parentheses, HTML/XML tags).


3. **Backtracking & State Traversal:**

* Executing Depth-First Search (DFS) on graphs, trees, or state-space decision trees.
* Implementing Undo/Redo operational histories (e.g., text editor command buffers, browser navigation history).


4. **Monotonic Stack Optimization:**

* Solving range-query problems (e.g., Next Greater Element, Largest Rectangle in Histogram) in linear time O (N) by
  keeping elements in strictly increasing or decreasing order inside the stack.