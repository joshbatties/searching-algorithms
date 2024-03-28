def breadth_first_search(graph, start):
     # Initialize a list to keep track of visited nodes, 
    # setting all elements to False indicating that no nodes have been visited yet.
    visited = [False] * len(graph)
    # Initialize a queue to keep track of nodes that need to be visited.
    queue = []
    # Add the starting node to the queue.
    queue.append(start)
    # Mark the starting node as visited.
    visited[start] = True
    # While the queue is not empty, visit the next node in the queue.
    while queue:
        # Get the next node from the queue.
        vertex = queue.pop(0)
        # Print the node.(for order of traversal)
        print(vertex)
        # For each neighbor of the current node, if the neighbor has not been visited yet, add it to the queue and mark it as visited.
        for v in graph[vertex]:
            if not visited[v]:
                queue.append(v)
                visited[v] = True





