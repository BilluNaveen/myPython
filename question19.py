def function_practice(a, b):
    sum=0
    for i in a:
        sum=sum+i
    return (sum/b)

    #in case if you have floor values we can use(//)

n=[1,2,4,5,6]
m=len(n)
print(function_practice(n,m))