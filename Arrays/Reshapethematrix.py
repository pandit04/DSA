def matrixreshape(mat,r,c):
    m= len(mat)
    n =len(mat[0])

    if m*n != r*c:
        return mat

    result =[[0]* c for _ in range(r)]
    k =0

    for i in range(m):
        for j in range(n):
            result[k // c][k % c] = mat[i][j]
            k= k+1
    return result

mat = [[1, 2], [3, 4]]
r=1
c=4
print(matrixreshape(mat,r,c))
        