from sys import maxsize

INF = int(maxsize)


def floyd_warshall(W):
    n = W.__len__()
    parent = [[-1 for i in range(n)] for j in range(n)]
    for k in range(n):
        for j in range(n):
            for i in range(n):
                if W[i][j] > W[i][k] + W[k][j]:
                    W[i][j] = W[i][k] + W[k][j]
                    parent[i][j] = k
    return W, parent


graph = [[0, 18, INF, 1, 5], [9, 0, 3, 2, INF], [INF, INF, 0, 4, INF], [INF, INF, 2, 0, 3], [3, INF, INF, INF, 0]]
result = floyd_warshall(graph)
print('Shortest path matrix: ' + str(result[0]))
print('Parent matrix: ' + str(result[1]))
