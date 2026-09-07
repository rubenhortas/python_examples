### Graphs

A **Graph** is a non-linear data structure consisting of a finite set of **Vertices** (or nodes) connected by **Edges**
(links). Graphs model complex, non-hierarchical network relationships between entities.

* **Key Classifications:**
* **Directed vs. Undirected:** Edges have a explicit direction (A to B) or represent symmetric bidirectional
  relationships (A <-> B).
* **Weighted vs. Unweighted:** Edges carry scalar attributes (e.g., latency, distance, bandwidth) or treat all
  connections with uniform cost (1).
* **Cyclic vs. Acyclic:** Paths can return to a starting vertex or guarantee zero directed cycles (e.g., Directed
  Acyclic Graphs/DAGs).


* **When to Use:**
* **Network Topology & Routing:** Modeling physical/logical infrastructure, dynamic packet routing, and network flow
  optimization.
* **Dependency Resolution:** Managing build pipelines, package manager dependencies, or task scheduling DAGs (e.g.,
  Topological Sorting).
* **Pathfinding & Spatial Navigation:** Computing shortest/optimal paths across weighted domains (e.g., Dijkstra's, A*,
  Bellman-Ford algorithms).
* **Relationship Analysis:** Analyzing social networks, recommendation engines, or fraud-detection clusters using graph
  traversals (BFS/DFS).