c0=int(input("enter any non zero non negative integer : "))
steps=0
while c0!=1:
    if c0%2!=1:
        c0=c0//2
        print(c0)
    else:
        c0=(3*c0)+1
        print(c0)
    steps+=1
print("steps=", steps)
