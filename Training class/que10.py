n=int(input("Enter the number:"))
sum=0
flag=0
while(n):
    d=n%10
    sum+=d
    n//=10
    for i in range(2,int(sum**0.5)+1):
        if sum%i==0:
            flag=1
            break
    if flag==1:
        print("Not Googly")
    else:
        print("Googly")