def dfs(adj_matrix, label):
    n = len(adj_matrix)

    visited = {label}
    stack = [label]

    while stack:
        current_node = stack.pop()
        print(f"Currently at node: {current_node}\n")
        
        for neighbor in range(n):
            if adj_matrix[current_node][neighbor] == 1 and neighbor not in visited:
                visited.add(neighbor)
                print(f"Visited neighbor: {neighbor}\n")
                stack.append(neighbor)
                print(f"-> Added {neighbor} to stack\n")

    return list(visited)

print(dfs([[0, 1, 0, 0],
          [1, 0, 1, 0],
          [0, 1, 0, 1], 
          [0, 0, 1, 0]], 1))

