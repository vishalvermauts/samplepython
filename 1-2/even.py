import sys
def oddeven():
    num=None
    try:
        num=int(input("Enter any Number: "))
    except ValueError:
        print("Enter a Integer: ")
        
        #sys.exit("Error:")

    if num<0:
        print("Number is negative")
    else:
        if num%2==0:
            print("Number is even")
        else:
            print("number is odd")
    oddeven()
oddeven()