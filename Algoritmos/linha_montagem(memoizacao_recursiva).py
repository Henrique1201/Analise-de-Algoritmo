def linha_rec(a, t, e, x):
    n = len(a)

    f1 = [-1] * n
    f2 = [-1] * n


    def linha_rec_rec(linha, k):
        if linha == 1:
            if f1[k] != -1:
                return f1[k]
            f1[k] = min(
                linha_rec_rec(1, k-1),
                linha_rec_rec(2, k-1) + t[1][k]
            ) + a[0][k]
            return f1[k]
        
        else:
            if f2[k] != -1:
                return f2[k]
            f2[k] = min(
                linha_rec_rec(1, k-1) + t[0][k],
                linha_rec_rec(2, k-1)
            ) + a[1][k]
            return f2[k]
        
    z1 = linha_rec_rec(1, n-1)
    z2 = linha_rec_rec(2, n-1)

    return min(z1 + x[0], z2 + x[1])