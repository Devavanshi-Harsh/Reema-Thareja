a=['295743861',
    '431865927',
    '876192543',
    '387459216',
    '612387495',
    '549216738',
    '763524189',
    '928671354',
    '154938672'
   ]
n=input()
def suduko(a):
    optnl = ""
    for i in range(9):
        for j in range(1,9):
            if len(a[i])!=9 or a[i].count(f"{j}")>1:
                print("invalid entry")
                return print("enter your values again")
    for i in range(9):
        for j in range(9):
            optnl+=a[j][i]
        for k in range(1,9):
            if optnl.count(f"{k}") > 1:
                return print("not suduko")
        optnl=[]





suduko(a)
