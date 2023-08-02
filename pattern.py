n=5
for i in range(n):
    for j in range(n):
        if(i==0 or j==0):
            print("4", end=" ")
        if(i==1 and j>0) or (j==1 and i>0):
            print("3", end=" ")
        if(i==n-1 or j==n-1):
            print("4", end=" ")
    print("")