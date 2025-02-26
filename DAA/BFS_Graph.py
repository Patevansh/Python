def dfs_graph(v,adj_list):
    visited=[False]*(v+1)
    dfs_result=[]

    def dfs(node):
        visited[node]=True
        dfs_result.append(node)

        for n in adj_list[node]:
            if not visited[n]:
                dfs(n)
        
    dfs(0)

    return dfs_result

adj_list={0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
v=len(adj_list)
print(dfs_graph(v,adj_list))


# Given Adjacency List:

# adj_list = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}

# DFS Traversal:

# Start at vertex 0:

# Mark vertex 0 as visited.
# Add vertex 0 to the dfs_result list.
# Explore adjacent vertices of 0:
# Vertex 1 is not visited. Recursively call dfs(1).
# DFS(1):

# Mark vertex 1 as visited.
# Add vertex 1 to the dfs_result list.
# Explore adjacent vertices of 1:
# Vertex 2 is not visited. Recursively call dfs(2).
# DFS(2):

# Mark vertex 2 as visited.
# Add vertex 2 to the dfs_result list.
# Explore adjacent vertices of 2:
# Vertex 3 is not visited. Recursively call dfs(3).
# DFS(3):

# Mark vertex 3 as visited.
# Add vertex 3 to the dfs_result list.
# Explore adjacent vertices of 3:
# Vertex 1 is already visited.
# Vertex 2 is already visited.
# Backtrack to DFS(2):

# Since there are no more unvisited adjacent vertices of 2, backtrack to DFS(1).
# Backtrack to DFS(1):

# Since there are no more unvisited adjacent vertices of 1, backtrack to DFS(0).
# DFS(0):

# Explore adjacent vertices of 0:
# Vertex 2 is already visited.
# Vertex 1 is already visited.
# Final dfs_result:

# [0, 1, 2, 3]