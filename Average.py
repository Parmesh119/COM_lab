# def odd(sum,n):
#     for i in range(1,n+1,+1):
#         if(i%2!=0):
#             sum=sum+i
#     print(sum)
#     print(sum/n)

def inrange(n1,n2,sum):
    cnt=0
    for i in range(n1,n2+1,+1):
        if(i%2!=0):
            sum=sum+i
        cnt=cnt+1
    print(sum+" "+sum/cnt)


# n=int(input())
n1=int(input())
n2=int(input())
sum=0
print(inrange(n1,n2,sum))
# print(odd(sum,n))

