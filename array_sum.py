def ary_sum(n):
    sum=0
    for i in ar:
        sum=sum+i
    print(sum)

m=input()
ar=list(map(int, input().rstrip().split()))
ary_sum(ar)
    