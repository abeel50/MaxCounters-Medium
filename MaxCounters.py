def solution(N, A):
    # write your code in Python 3.6
    sol = [0] * N
    m = 0
    prv = 0
    for i in A:
        if i > 0 and i <= N:
            sol[i-1] += 1
            if sol[i-1] > m:
                m = sol[i-1]
        elif i == N + 1 and prv != N + 1:
            sol = [m] * N
        prv = i
    return sol