m = int(input("Enter the limit of the limit: "))
n = int(input("Enter the second limit of the limit: "))
for i in range (1,m+1):
    for y in range(1,n+1):
        print(str(i)+' * '+str(y)+' =',end=' ')
        print(i*y)