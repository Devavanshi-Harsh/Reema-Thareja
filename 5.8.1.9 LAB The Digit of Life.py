n=int(input("enter your birthday in MMDDYYYY format"))
def sum(n):
    s0=0
    n=str(n)
    for i in n:
        s0+=int(i)
    if s0<10:
        return s0
    return sum(s0)
print(sum(n))