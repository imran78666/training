a=int(input("weight of limak:"))
b=int(input("weight of bob:"))

years=0

while a<=b:
    a*=3
    b*=2
    years+=1

print(years)