
r=int(input("Enter the Range of list: "))
I=[]
for i in range(r):
    i=int(input("Enter the nums: "))
    I.append(i)
print("Nums = ",I)
m=I.copy()
def smallnum(o):
    c=0
    for i in range(r):
        for j in range(r):
            if(I[i]!=m[j] and m[j]<I[i]):
                c=c+1
        print([c])
        c=0
smallnum(r)
