#Transpose Matrix 
X=[[1,2,4],[1,4,3],[6,4,4]]
R=[[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(X)):
    for j in range(len(X[0])):
        R[j][i]=X[i][j]

for y in R:
    print(y)