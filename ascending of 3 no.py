a = int(input("Enter no. : "))
b = int(input("Enter no. : "))
c = int(input("Enter no. : "))
mx,mn,md=a,a,0
if(b>mx):
    mx=b
if(c>mx):
    mx=c
if(b<mn):
    mn=b
if(c<mn):
    mn=c
md=(a+b+c)-(mx+mn)
print("Ascending order is : "+str(mn)+","+str(md)+","+str(mx))
