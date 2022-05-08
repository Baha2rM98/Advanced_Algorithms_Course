def binomial_coefficient_recursive(n, k):
    if k == 0 or n == k:
        return 1
    return binomial_coefficient_recursive(n - 1, k - 1) + binomial_coefficient_recursive(n - 1, k)


def binomial_coefficient_dp(n, k):
    B = [[0 for x in range(k + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            if j == 0 or j == i:
                B[i][j] = 1
            else:
                B[i][j] = B[i - 1][j - 1] + B[i - 1][j]
    return B[n][k]


print(binomial_coefficient_dp(17, 9))
print(binomial_coefficient_recursive(17, 9))
