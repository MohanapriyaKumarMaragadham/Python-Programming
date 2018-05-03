def lcs(S,T):
    m = len(S)
    n = len(T)
    counter = [[0]*(n+1) for x in range(m+1)]
    longest = 0
    w= set()
    for i in range(m):
        for j in range(n):
            if S[i] == T[j]:
                c = counter[i][j] + 1
                counter[i+1][j+1] = c
                if c > longest:
                    w= set()
                    longest = c
                    w.add(S[i-c+1:i+1])
                elif c == longest:
                    w.add(S[i-c+1:i+1])

    return w
a=raw_input()
b=raw_input()
ret = lcs(a,b)
for s in ret:
    print s
