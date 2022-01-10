mapgrid = [10,10]
print(mapgrid)
n = 10
for row in range(0,n):
    if row == 0 or col == 0 or row==n-col-1:
        print("*")
    print()