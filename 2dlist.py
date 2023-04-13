r = int(input("Enter no. of rows : "))
c = int(input("Enter no of columns : "))
arr=[]
for i in range(0,r,1):
    a=[]
    print("Enter values row wise.")
    for j in range(0,c,1):
        a.append(int(input("Enter the element : ")))
    arr.append(a)

print(arr)
        
