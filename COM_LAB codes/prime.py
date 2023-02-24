def prime(n):
    f=False
    for i in range(2,n,+1):
        if(n%i==0):
            return False
    return True


n1=int(input())
n2=int(input())
if(n1==1 and n2!=1):
    n1=n1+1
elif(n1==1 and n2==1):
    print("No prime numbers are there")

for i in range(n1,n2+1,+1):
    if(prime(i)):
        print(i)