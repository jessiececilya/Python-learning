X=[[1,2,4],
[1,4,3],
[6,4,4]]
Y=[[1,2,4],
[1,4,3],
[6,4,4]]
R=[[0,0,0],
[0,0,0],
[0,0,0]]

for i in range(len(X)):
    for j in range(len(Y[0])):
        for k in range(len(Y)):
            R[i][j] += X[i][k] * Y[k][j]

for r in R:
    print(r)