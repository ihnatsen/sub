from math import inf


def grasshopper(start, end, D):
    start-=1
    end-=1
    def arg_min(T, S):
        amin = -1
        m = inf
        for i, t in enumerate(T):
            if t < m and i not in S:
                m = t
                amin = i

        return amin

    N = len(D)
    T = [inf]*N

    v = 0
    S = {v}
    T[v] = 0
    M = [0]*N

    while v != -1:
        for j, dw in enumerate(D[v]):
            if j not in S:
                w = T[v] + dw
                if w < T[j]:
                    T[j] = w
                    M[j] = v

        v = arg_min(T, S)
        if v >= 0:
            S.add(v)


    P = [end]
    while end != start:
        end = M[P[-1]]
        P.append(end)

    print([item+1 for item in P[::-1]])
    print(T)


paths = [[0,  7, 10, inf, inf, inf],
         [7,  0,  6, 8, inf, inf],
         [10, 6, 0, 2, 3, inf],
         [inf,  8, 2, 0, 7, 8],
         [inf,  inf, inf, 7, 0, 9],
         [inf,  inf, inf, inf, 9, 0]]
start = 1
end = 6
grasshopper(start, end, paths)
