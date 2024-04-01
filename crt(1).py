def simpleInterest(p,t,r):
    si=(p*t*r)/100
    print(si)
def compoundInterest(p,t,r):
    A=p*(1+r/100)**t
    ci=A-p
    print(ci)
def arm(x):
    n=x
    l=len(str(x))
    s=0
    while(n!=0):
        r=n%10
        s=s+(r**l)
        n=n//10
    if(s==x):
        print("yes")
    else:
        print("no")
arm(int(input()))
def pallindrome(x):
    n=x
    r=0
    s=0
    while(n!=0):
        r=n%10
        s=s*10+r
        n=n//10
    if(s==x):
        print("yes")
    else:
        print("no")
def fact(x):
    c=x
    s=1
    while(c!=0):
        s=s*c
        c=c-1
    print(s)
fact(int(input()))
def per(x):
    n=1
    c=0
    while(n<x):
        if(x%n==0):
            c=c+n
        n=n+1
    if(c==x):
        print("perfect")
    else:
        print("np")
def sumnatural_numbers(x):
    s=0
    n=1
    while(n<=x):
        s=s+n
        n=n+1
    print(s)
def pattern1(x):
    for i in range(1,x):
        for j in range(1,i+1):
            print(j,end=' ')
        print()
def pattern2(x):
    for i in range(x):
        for j in range(i,i+1):
            print(" "*(x-i),'* '*(i+1),end=' ')
        print()
def pattern3(x):
    n=x
    for i in range(1,4):
        for j in range(1,5):
            print(n,end=' ')
            n=n+1
        print()