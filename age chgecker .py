def agechecker(age):
    if(age>18):
        return 1
    else :
        return 0

n=int(input("enter your age"))
con=agechecker(n)

if(con==1):
    print("you can go")
else :
    print("you can't go6")