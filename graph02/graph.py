

def luDecomposition(mat, n):

    lower = [[0 for x in range(n)]
             for y in range(n)]
    upper = [[0 for x in range(n)]
             for y in range(n)]

    for i in range(n):

        for k in range(i, n):

            sum = 0
            for j in range(i):
                sum += (lower[i][j] * upper[j][k])

            upper[i][k] = mat[i][k] - sum

        for k in range(i, n):
            if (i == k):
                lower[i][i] = 1
            else:

                sum = 0
                for j in range(i):
                    sum += (lower[k][j] * upper[j][i])

                lower[k][i] = int((mat[k][i] - sum) /
                                  upper[i][i])

    f = open("input.txt", "w")

    f.write(str(n))
    f.write('\n')
    for i in range(n):
        for j in range(n):
            if j != 0:
                f.write(" ")

            f.write(str(mat[i][j]))
        f.write('\n')

    f.write('\n\n\n')

    print("Lower Triangular")
    f.write("\nLower Triangular\n")

    for i in range(n):

        for j in range(n):
            print(lower[i][j], end="\t")
            f.write(str(lower[i][j]))
            f.write('\t')
        print("")
        f.write('\n')

    print("Upper Triangular")
    f.write("\nUpper Triangular\n")

    for i in range(n):
        for j in range(n):
            print(upper[i][j], end="\t")
            f.write(str(upper[i][j]))
            f.write('\t')
        print("")
        f.write('\n')

    f.close()


f = open('input.txt', "r")
n = int(f.readline())

mat = [[0 for x in range(n)] for y in range(n)]

for i in range(n):
    line = f.readline()
    x = line.split()
    for j in range(n):
        mat[i][j] = int(x[j])

'''
mat = [[2, -1, -2],
       [-4, 6, 3],
       [-4, -2, 8]]
'''

f.close()

luDecomposition(mat, n)
