N,X=map(int,input().split())
li=[N]
li=map(int,input().split())

if X in li:
    if X/2==0:
        print("Even Number")
    else:
        print("Odd Number")
else:
    print("Number is'nt exist in list")
