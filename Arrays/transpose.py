def transpose(matrix):
    rows = len(matrix)
    columns = len(matrix[0])

    result =[]

    for j in range(columns):
        row =[]
    
    for i in range(rows):
        row.append(matrix[i][j])
        result.append(row)

    return result

matrix =[[1,2],[3,4]]
print(transpose(matrix))