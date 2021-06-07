def pos(a,b):
    for i in b:
        c=a.find(i)
        if c==-1:
            return print("string is not present")
    return print("present")

a="Nabucodonosor".lower()
b="donur".lower()
pos(a,b)

