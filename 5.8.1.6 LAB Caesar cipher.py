cipher=input("enter the code to be encrypted")
n=int(input("enter the place to be shifted"))
encryption=""
for c in cipher:
        if c.isspace():
            code=" "
        if c.isupper():
            code=(ord(c)+n)
            if code>90:
                code-=26
            code=chr(code)
        elif c.islower():
            code=(ord(c)+n)
            if code>122:
                code-=26
            code=chr(code)
        elif c.isdigit():
            code=c

        encryption+=code
print(encryption)