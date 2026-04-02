def lcs_dp(v, a, b):
    M = find_value(v, a, b)
    max_v = M[len(a)][len(b)]
    lcs = find_solution(v, a, b, len(a), len(b), M, "")
    return max_v, lcs

def find_value(v, a, b):
    # Source for help creating a 2d list pre-allocated with 0: https://www.geeksforgeeks.org/python/python-using-2d-arrays-lists-the-right-way/
    M = [[0 for n in range(len(b) + 1)] for m in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                M[i][j] = max(M[i-1][j-1] + v[a[i-1]], M[i-1][j-1], M[i][j-1])
            else:
                M[i][j] = max(M[i-1][j], M[i][j-1])
    return M             

def find_solution(v, a, b, i, j, M, curr=""):
    if i == 0 or j == 0:
        return curr + ""
    elif a[i - 1] == b[j - 1] and M[i][j] == M[i-1][j-1] + v[a[i-1]]:
        return curr + find_solution(v, a, b, i-1, j-1, M, curr) + a[i - 1]
    elif M[i][j] == M[i-1][j]:
        return curr + find_solution(v, a, b, i-1, j, M, curr)
    else:
        return curr + find_solution(v, a, b, i, j-1, M, curr)  