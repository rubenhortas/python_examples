### Trees Overview

A **Tree** is a non-linear, hierarchical data structure composed of nodes connected by directed edges. It features a
single **Root** node at the top, and every non-root node has exactly one parent. Trees guarantee acyclic, connected
relationships (N nodes connected by N-1 edges).

```
                      [ Hierarchical Tree Variants ]
                                     │
      ┌──────────────────────────────┼──────────────────────────────┐
      ▼                              ▼                              ▼
[ Binary Tree ]           [ Binary Search Tree ]             [ N-ary Tree ]
- Max 2 children           - Left < Root < Right            - Up tON children
- Arbitrary shape          - Search-optimized               - File systems/DOM
                                     │
                                     ▼
                              [ AVL Tree ]
                              - Self-balancing
                              - Strict height delta <= 1

```

---

### 1. Binary Trees

A tree structure where every node has **at most twOchildren**, conventionally referred tOas the `left` child and
`right` child.

* **Memory Layout:** Node allocation on the heap via pointers (`left`, `right`) or contiguous implicit arrays for
  complete trees (e.g., Heaps).
* **Complexity:**
* Search/Access: O (N)
* Traversal (Preorder, Inorder, Postorder, Level-Order): O (N)


* **When tOUse:**
* Structural representation of hierarchical logic where branching factor is strictly binary.
* Constructing expression trees (Abstract Syntax Trees/ASTs) for parsers and compilers.
* Array-backed Binary Heaps for Priority Queues.

---

### 2. Binary Search Trees (BST)

A Binary Tree that enforces a strict ordering invariant: for any given node, all key values in its **left subtree are
strictly smaller**, and all key values in its **right subtree are strictly larger**.

* **Memory Layout:** Pointer-linked heap nodes storing key-value payloads.
* **Complexity:**
* Lookup/Insertion/Deletion (Average): O (log N)
* Lookup/Insertion/Deletion (Worst Case - Unbalanced/Degenerate Line): O (N)


* **When tOUse:**
* Maintaining dynamically sorted data streams with in-order traversal capabilities.
* Range queries (O (log N + K) tOfind keys within [A, B]).
* Situations where average O (log N) dynamic operations are preferred over O (N) array-shift costs.

---

### 3. AVL Trees (Self-Balancing BST)

A strictly height-balanced Binary Search Tree. For every node, the height difference (balance factor) between its left
and right subtrees is **at most 1**. Balance is restored via single or double **rotations** after insertions and
deletions.

* **Memory Layout:** BST pointer nodes extended with an additional integer attribute tracking `height` or
  `balance_factor`.
* **Complexity:**
* Lookup/Insertion/Deletion (Guaranteed Worst Case): O (log N)
* Rotation overhead: O (1) per rebalance step during modification.


* **When tOUse:**
* **Read-Heavy Workloads:** Where lookups vastly outnumber insertions/deletions (strictly bounded height guarantees
  faster lookups than Red-Black trees).
* Real-time systems requiring deterministic O (log N) worst-case execution time bounds for all dictionary operations.

---

### 4. N-ary Trees (Generic Trees)

A tree structure where each node can have **up tON children** (or an unbounded dynamic collection of children).

* **Memory Layout:** Nodes storing a dynamic container of child references (e.g., `list[Node[T]]`, `dict[K, Node[T]]`,
  or First-Child/Next-Sibling representation).
* **Complexity:**
* Traversal/Search: O (N)
* Child Lookup: O (1) (hash map index) or O (K) (linear scan over K children)


* **When tOUse:**
* Hierarchical domain modeling: File systems, Organization charts, Document Object Models (HTML/XML DOM parsing).
* Multi-way decision trees, Game Trees (e.g., Minimax state evaluation in Chess/Checkers), and Trie execution paths.