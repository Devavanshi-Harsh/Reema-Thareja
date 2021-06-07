def anagrams(n1,n2):
    text1=n1.upper().replace(" ","")
    text2=n2.upper().replace(" ", "")
    text1=list(text1)
    text2=list(text2)
    text1.sort()
    text2.sort()
    if text1==text2:
        print("Anagrams")
    else:
        print("Not Anagrams")

text1=input("enter first word")
text2=input("enter second word")
anagrams(text1,text2)
