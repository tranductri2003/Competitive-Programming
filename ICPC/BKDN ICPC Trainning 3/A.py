while True:
    n=int(input())
    if n==0:
        break
    else:
        a=list(map(int,input().split()))
        res=0
        for i in range(1,n-1):
            if a[i]> a[i-1] and a[i]>a[i+1]:
                res+=1
        print(res)