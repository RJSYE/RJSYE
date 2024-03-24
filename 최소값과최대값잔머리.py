N = int(input())
A = list(map(int,input().split()))[:N]
larg = -1000000000000
smal = 9999999999
for i in A:
    if i > larg:
        larg = i
    if i < smal:
        smal = i
print(str(smal)+' '+str(larg))
