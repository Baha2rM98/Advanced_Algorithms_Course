from sys import maxsize

MAX = int(maxsize)


def matrix_chain_multiplication_cost(n, d):
    m = [[0 for i in range(n)] for j in range(n)]
    for L in range(2, n + 1):
        for i in range(n - L + 1):
            j = i + L - 1
            m[i][j] = MAX
            for k in range(i, j):
                q = (m[i][k] + m[k + 1][j] +
                     (d[i] * d[k + 1] * d[j + 1]))
                if q < m[i][j]:
                    m[i][j] = q
                    m[j][i] = k + 1
    return m


def print_chain_by_order(m, j, i):
    if j == i:
        print(chr(65 + j), end='')
        return
    else:
        print('(', end='')
        print_chain_by_order(m, m[j][i] - 1, i)
        print_chain_by_order(m, j, m[j][i])
        print(')', end='')


arr = [5, 2, 3, 4, 6, 7, 8]
size = len(arr) - 1
result = matrix_chain_multiplication_cost(size, arr)
print('Optimal number of multiplications is: ' + str(result[0][size - 1]))
print('Optimal presentation is: ', end='')
print_chain_by_order(result, size - 1, 0)
