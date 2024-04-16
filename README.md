# searching-algorithms
A collection of all the searching algorithms introduced in Monash University's FIT2004: Algorithms and Data Structures

# Breadth-First-Search
Breadth-first search (BFS) is an algorithm used for traversing or searching tree or graph data structures.
I have implemented the BFS algorithm with the graph represented as a list of lists.
It starts at a selected node (the "root" in a tree, or any arbitrary node in a graph) and explores all of the neighbor nodes at the present depth (same distance from the source)prior to moving on to the nodes at the next depth level. BFS is particularly useful for finding the shortest path on unweighted graphs.

A step by step implementation of BFS:
1. Start by putting any one of the graph's vertices at the back of a queue.
2. Take the front item of the queue and add it to the visited list.
3. Create a list of that vertex's adjacent nodes. Add the ones which aren't in the visited list to the back of the queue.
4. Keep repeating steps 2 and 3 until the queue is empty.

Assumptions:
This implementation assumes that graph is represented as a list of lists, where each sublist contains the indices of adjacent nodes. The indices are assumed to correspond to nodes in a 0-indexed manner.
The start parameter is an index into the graph list, representing the starting node for the BFS traversal.

Time Complexity:
BFS is O(V + E) for a graph represented using an adjacency list, where V is the number of vertices and E is the number of edges in the graph. 
This is because every vertex and every edge will be explored in the worst-case scenario.
Vertices (V): Each vertex is pushed to the queue exactly once.
Edges (E): Each edge is considered exactly once. For every vertex, all its adjacent edges/nodes are explored.

Space Complexity
O(V), not including the space to store the graph itself
The space complexity of BFS primarily depends on the size of the queue that is used to store the vertices to be explored. In the worst case, the queue might need to hold all the vertices of the graph, which makes the space complexity O(V).
Visited List: Uses O(V) space.
Queue: In the worst case, when the graph is fully connected, the queue could hold all vertices except the starting vertex before starting to dequeue, also resulting in O(V) space.

# Depth-First-Search
Depth-first search (DFS) is an algorithm used for traversing or searching tree or graph data structures.
I have implemented the DFS algorithm with the graph represented as a list of lists.
The algorithm initiates from a specified start node and explores as deep as possible into the graph's branches before backtracking.

A step-by-step implementation of DFS:
1. Begin with marking the initial node as visited and push it onto the stack.
2. Pop a node from the stack to examine it and mark it as visited.
3. Retrieve a list of adjacent nodes for the popped node. For each adjacent node that has not been visited, mark it as visited and push it onto the stack.
4. Repeat steps 2 and 3 until the stack is empty.

Assumptions
The DFS implementation assumes the graph is represented as a list of lists, with each sublist containing the indices of adjacent nodes. These indices correspond to nodes in a 0-indexed manner. 
The 'start' parameter is an index into the graph list, denoting the starting node for the DFS traversal.

Time Complexity:
DFS is O(V + E) for a graph represented using an adjacency list, where V is the number of vertices and E is the number of edges. This efficiency results from each vertex being explored once and each edge being examined once in the process. For every visited vertex, the algorithm checks each of its edges once.
Vertices (V): Each vertex is explored exactly once.
Edges (E): Each edge in the graph is considered once, ensuring that all nodes reachable from the starting node are visited.

Space Complexity:
The space complexity of DFS is O(V), excluding the space required to store the graph itself. This complexity stems from the storage requirements of the stack and the visited list, which in the worst-case scenario, might need to hold all vertices of the graph.
Visited List: Utilizes O(V) space to track whether each vertex has been visited.
Call Stack: In the deepest possible scenario, the stack might contain a path from the root to a leaf node in a tree, or a long unbroken chain of vertices in a graph. This scenario also results in O(V) space complexity.
