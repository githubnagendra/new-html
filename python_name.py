import sys
while True:
    name =(input("enter your name : "))
    x=len(name)
    if x>5:
     if name.isalpha():
        print("hello.......!,welcome",name,"......!")
     
    else:
            print("Your Name has less than 5 Letters Please Give Greater than 5 Letters")