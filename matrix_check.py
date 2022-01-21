from matrix import Matrix


def all_right(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != matrix[j][i]:
                return False, (i, j)
    return True, (-1, -1)


matrix = Matrix()._matrix
check, problem = all_right(matrix)
if check:
    print('All Right!')
else:
    print(f'Not Correct: {problem[0]}, {problem[1]}')
