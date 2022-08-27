fiboArr = [0,1]

def get(n):
    for i in range(2,n):
        fiboArr.append(fiboArr[i-1]+fiboArr[i-2])
    return fiboArr

    
def getMod(n,k):
    get(k)
    count = 0;
    for i in fiboArr:
        fiboArr[count] = fiboArr[count]%n
        count+=1
    return fiboArr


# print(getMod(5,56))

# a = {1: 23, 2:76, 3:27}
# for i in a:
#     print(a[i])
