n,m,a,b = map(int,input("enter ther integers").split())
if a*m<b:
    print(n*a)
else:
    print((n//m)*b+min(n%m*a,b))