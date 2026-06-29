def adjacency_list_to_matrix(adj_list) -> list:
    n = len(adj_list)
    # assumes nodes are 0-indexed integers
    adj_matrix = [[0] * n for _ in range(n)]

    for node in adj_list:
        for edge in adj_list[node]:
            adj_matrix[node][edge] = 1
        print(adj_matrix[node])

    return adj_matrix

adj_list = {0: [2], 
            1: [2, 3], 
            2: [0, 1, 3], 
            3: [1, 2]}

print(adjacency_list_to_matrix(adj_list))