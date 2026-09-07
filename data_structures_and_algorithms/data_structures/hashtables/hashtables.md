### Hash Tables

A **Hash Table** (or Hash Map) is a data structure that implements an associative array, mapping keys to values using a
**hash function** to compute an index into a bucket array.

* **Key Characteristics:** Provides average $O (1)$ time complexity for lookup, insertion, and deletion operations by
  distributing keys deterministically across memory.
* **When to Use:**
* **$O (1)$ Lookups & Indexing:** When constant-time key-based retrieval is required over large datasets.
* **Uniqueness & Deduplication:** When tracking distinct elements or detecting duplicates efficiently (e.g., Set
  semantics).
* **Frequency Counting & Caching:** Ideal for building index maps, memoization tables, or counting frequencies (e.g.,
  histogram construction).