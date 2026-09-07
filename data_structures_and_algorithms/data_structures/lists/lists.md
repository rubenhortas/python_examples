### Lists Overview

A **List** is a linear data structure representing a sequential collection of elements. The underlying memory layout and
performance profiles vary fundamentally depending on the specific implementation variant.

```
                      [ Linear List Structures ]
                                  │
      ┌───────────────────────────┼───────────────────────────┐
      ▼                           ▼                           ▼
[ Dynamic Array ]         [ Linked List ]             [ Ring Buffer ]
- Contiguous memory       - Pointer-linked nodes      - Fixed circular array
- Cache-line friendly     - Random heap allocs        - Head/Tail index offsets
- O(1) random access      - O(N) traversal access     - O(1) Push/Pop both ends

```

---

### 1. Dynamic Arrays (Standard Array-Backed Lists)

Contiguous blocks of memory that automatically resize when capacity limits are reached (e.g., Python `list`, C++
`std::vector`, Rust `Vec`, C# `List<T>`).

* **Memory Layout:** Contiguous heap block. Excellent CPU cache line prefetching.
* **Complexity:**
* Random Access (A[i]): O (1)
* Append (End): O (1) amortized
* Insertion / Deletion (Arbitrary Index): O (N) due to element shifting


* **When to Use:**
* Default, general-purpose choice for sequential data.
* When fast O (1) index-based access or iteration over contiguous memory is required.
* When size changes primarily occur at the end of the collection.

---

### 2. Linked Lists (Singly & Doubly Linked)

Nodes distributed non-contiguously across memory, where each node explicitly stores its data payload alongside one or
two pointers to adjacent nodes.

* **Memory Layout:** Scattered heap allocations connected via explicit heap pointers. High pointer overhead and poor CPU
  cache locality.
* **Complexity:**
* Random Access (A[i]): O (N)
* Insertion / Deletion at Known Iterator/Node: O (1)
* Prepending (Head Insertion): O (1)


* **When to Use:**
* High-frequency O (1) insertions/deletions at arbitrary positions *after* obtaining a valid iterator/node reference.
* Real-time or embedded applications where array reallocation spikes (O (N) amortized copy overheads) cannot be
  tolerated.
* Building low-level lock-free queues, stacks, or memory allocators.

---

### 3. Rotating Lists (Circular Buffers / Ring Buffers / Deques)

Fixed or dynamically bounded collections operating on a contiguous array with two logical pointers (`head` and `tail`)
that wrap around using modulo arithmetic (`index % capacity`).

* **Memory Layout:** Contiguous array with wrapping offset pointers. Excellent cache locality without element shifting
  during rotations.
* **Complexity:**
* Push / Pop at Head or Tail: O (1)
* Rotation Shift (`shift_left` / `shift_right` by K positions): O (1) logic offset manipulation (or O (K) if physically
  mutating elements)
* Random Access: O (1) via offset calculation (`(head + i) % capacity`)


* **When to Use:**
* Producer-Consumer bounded queues, ring buffers, and streaming audio/video I/O pipelines.
* Sliding-window algorithms requiring fixed-capacity retention.
* Fast O (1) double-ended queue operations (e.g., Python `collections.deque`, Rust `VecDeque`).