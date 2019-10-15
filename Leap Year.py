n=int(input("Enter the Year: "))
if n%4!=0:
    print("The Year",n,"is NOT Leap Year.")
if n%4==0:
    if n%100==0:
        if n%400==0:
            print("The Year",n,"is a Leap Year.")
        if n%400!=0:
            print("The Year",n,"is NOT Leap Year.")
    else :
        print("The Year",n,"is a Leap Year.")
