# searching-algorithms
A collection of all the searching algorithms introduced in Monash University's FIT2004: Algorithms and Data Structures

# Breadth-First-Search
Breadth-first search (BFS) is an algorithm used for traversing or searching tree or graph data structures. It starts at a selected node (the "root" in a tree, or any arbitrary node in a graph) and explores all of the neighbor nodes at the present depth (same distance from the source)prior to moving on to the nodes at the next depth level. BFS is particularly useful for finding the shortest path on unweighted graphs.

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