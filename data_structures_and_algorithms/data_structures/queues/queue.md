### Queue

A **Queue** is a linear data structure operating on a **First-In, First-Out (FIFO)** processing principle: the first
element inserted is the first to be removed.

A **Priority Queue** is an abstract extension where each element carries an associated priority scalar. Elements are
dequeued based on priority order rather than insertion order (typically implemented using binary heaps).

```
[ Standard FIFO Queue ]
Enqueues (Rear) ──► [ Element 3 ] [ Element 2 ] [ Element 1 ] ──► Dequeues (Front)

[ Min-Priority Queue (Heap-Backed) ]
Push (Arbitrary) ──► [ Node (Priority: 10) ]
                     [ Node (Priority: 5)  ] ──► Pop Highest Urgency (Priority: 1)
                     [ Node (Priority: 1)  ]

```

---

### 1. Standard FIFO Queues

Elements are appended to the rear and evicted from the front, maintaining strict execution order.

* **Underlying Implementations:** Circular arrays / ring buffers, doubly linked lists, or two-stack array abstractions.
* **Complexity:**
* Enqueue (Push): O (1)
* Dequeue (Pop): O (1)
* Peek (Front): O (1)


* **When to Use:**
* **Asynchronous Buffer / Producer-Consumer:** Decoupling thread execution using bounded channels (e.g., thread pools,
  message brokers like RabbitMQ or Kafka).
* **Level-Order Traversals:** Breadth-First Search (BFS) in trees and graphs.
* **Resource Scheduling:** First-come, first-served handling of shared hardware resources (e.g., CPU task scheduling,
  print queues, disk I/O request queues).

---

### 2. Priority Queues (Min-Heap / Max-Heap)

An associative ordering structure where every insertion positions the element according to its priority ranking relative
to existing nodes.

* **Underlying Implementations:** Array-backed Binary Heaps, Fibonacci Heaps, or Pairing Heaps.
* **Complexity:**
* Push (Insertion): O (\log N)
* Pop Min/Max (Eviction): O (\log N)
* Peek Min/Max: O (1)
* Heapify (Array build): O (N)


* **When to Use:**
* **Priority Task Execution:** Executing operating system processes, network packet routing, or event-driven simulation
  steps based on dynamic deadlines rather than arrival time.
* **Greedy Graph Algorithms:** Shortest path searches (**Dijkstra's**, **A***) and Minimum Spanning Trees (**Prim's**).
* **Streaming Top-K Retention:** Maintaining the top K items in real-time streaming data within an bounded O (K)
  heap.
* **Data Compression:** Constructing optimal prefix codes in **Huffman Coding**.