def count(statement,cnt):
    vw=['a','A','e','E','i','I','o','O','u','U']
    for i in range(len(statement)):
        if(statement[i] in vw):
            cnt=cnt+1
    return cnt

statement=input()
cnt=0
print(count(statement,cnt))
