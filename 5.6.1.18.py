def mysplit(strng):
    li=[]
    strng2=""
    for i in strng:
        if i.isalpha():
            strng2+=i
        else:
            li.append(strng2)
            strng2=""
            for i in li:
                if i=="":
                    li=[]
    return li


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
