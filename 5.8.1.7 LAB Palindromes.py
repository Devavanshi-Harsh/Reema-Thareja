def ispalindrom(strg):
    strg1=strg.upper()
    strg1=strg1.replace(" ","")
    strg2=""

    strg2=strg1[::-1]

    if strg1==strg2:
        print(f"*{strg}* is a palindrome")
    else:
        print(f"*{strg}* is not a palindrome")

checkingst=input("enter a sentence to check palindrome")
ispalindrom(checkingst)
